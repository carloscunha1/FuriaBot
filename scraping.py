from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def iniciar_driver():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("--headless") 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def aceitar_cookies(driver):
    try:
        print("🔍 Procurando botão de cookies...")
        
        cookie_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
        )
        
        try:
            cookie_btn.click()
        except:
            driver.execute_script("arguments[0].click();", cookie_btn)
        
        print("✅ Cookies aceitos com sucesso.")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao aceitar cookies: {e}")
        return False

def buscar_noticias():
    try:
        driver = iniciar_driver()
        print("🌐 Acessando página da FURIA...")
        driver.get("https://www.hltv.org/team/8297/furia")
        
        if not aceitar_cookies(driver):
            print("⚠️ Não foi possível aceitar os cookies, mas tentando continuar...")
        
        print("📰 Navegando para a seção de notícias...")
        time.sleep(2)
        
        news_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.tab[data-content-id="newsBox"]'))
        )
        news_tab.click()
        
        time.sleep(3)

        noticias = driver.find_elements(By.CSS_SELECTOR, 'a.subTab-newsArticle')
        noticias_info = []

        for noticia in noticias[:5]:  # Limita a 5 notícias
            try:
                data = noticia.find_element(By.CSS_SELECTOR, 'span.subTab-newsDate').text
                titulo = noticia.text.replace(data, '').strip()
                
                href = noticia.get_attribute('href')
                link = href if href.startswith('https://') else f"https://www.hltv.org{href}"
                
                noticia_formatada = f"📰 {titulo}\n📅 {data}\n🔗 {link}\n"
                noticias_info.append(noticia_formatada)
                
            except Exception as e:
                print(f"Erro ao processar notícia: {e}")
                continue

        driver.quit()
        return noticias_info if noticias_info else "Nenhuma notícia encontrada."
        
    except Exception as e:
        print(f"Erro detalhado: {e}")
        if driver:
            driver.quit()
        return f"Erro ao buscar notícias: {str(e)}"

def buscar_proximos_jogos():
    driver = None
    try:
        driver = iniciar_driver()
        print("🌐 Acessando página da FURIA...")
        driver.get("https://www.hltv.org/team/8297/furia")
        
        if not aceitar_cookies(driver):
            print("⚠️ Não foi possível aceitar os cookies, mas tentando continuar...")
        
        print("🎮 Navegando para a seção de partidas...")
        time.sleep(2)
        
        matches_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.tab[data-content-id="matchesBox"]'))
        )
        matches_tab.click()
        
        time.sleep(3)

        jogos = driver.find_elements(By.CSS_SELECTOR, '.team-row')
        jogos_info = []

        for jogo in jogos[:5]: 
            try:
                data = jogo.find_element(By.CSS_SELECTOR, '.date-cell span').get_attribute('data-unix')
                data_formatada = time.strftime('%d/%m/%Y', time.localtime(int(data)/1000))

                times = jogo.find_elements(By.CSS_SELECTOR, '.team-name')
                if len(times) >= 2:
                    time1 = times[0].text.strip()
                    time2 = times[1].text.strip()
                    
                    jogo_info = f"🆚 {time1} vs {time2}\n📅 {data_formatada}\n"
                    jogos_info.append(jogo_info)
                
            except Exception as e:
                print(f"Erro ao processar jogo: {e}")
                continue

        driver.quit()
        return jogos_info if jogos_info else "Nenhum jogo agendado encontrado."
        
    except Exception as e:
        print(f"Erro detalhado: {e}")
        if driver:
            driver.quit()
        return []  
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

if __name__ == "__main__":
    print("🔍 Notícias:")
    for noticia in buscar_noticias():
        print(noticia)

    print("\n🕹️ Próximos Jogos:")
    for jogo in buscar_proximos_jogos():
        print(jogo)
