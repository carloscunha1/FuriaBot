import telebot
from telebot import types
from scraping import buscar_proximos_jogos, buscar_noticias
from config import TELEGRAM_API_KEY
import time
import random

bot = telebot.TeleBot(TELEGRAM_API_KEY)

perguntas_feitas = []
MAX_PERGUNTAS_MEMORIA = 8
user_states = {} 

@bot.message_handler(commands=['start'])
def start(msg):
    print(f"Comando /start recebido de {msg.chat.id}")
    markup = types.InlineKeyboardMarkup()
    btn_jogos = types.InlineKeyboardButton("🎯 Jogos", callback_data="jogos")
    btn_noticias = types.InlineKeyboardButton("📰 Notícias", callback_data="noticias")
    btn_quiz = types.InlineKeyboardButton("🎮 Jogo de Perguntas", callback_data="quiz")
    btn_redes_sociais = types.InlineKeyboardButton("🔗 Redes Sociais", callback_data="redes_sociais")
    markup.add(btn_jogos, btn_noticias, btn_quiz, btn_redes_sociais)

    bot.send_message(msg.chat.id, "🎯 Bem-vindo ao Bot da FURIA!\nEscolha uma opção:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "jogos")
def jogos(call):
    jogos = buscar_proximos_jogos()
    if isinstance(jogos, list) and jogos:  # Verifica se é uma lista e não está vazia
        for jogo in jogos:
            bot.send_message(call.message.chat.id, jogo)
    else:
        bot.send_message(call.message.chat.id, "Nenhum jogo encontrado no momento.")

@bot.callback_query_handler(func=lambda call: call.data == "noticias")
def noticias(call):
    noticias = buscar_noticias()
    if isinstance(noticias, list):
        for noticia in noticias:
            bot.send_message(call.message.chat.id, noticia)
    else:
        bot.send_message(call.message.chat.id, noticias)

@bot.callback_query_handler(func=lambda call: call.data == "quiz")
def quiz(call):
    global perguntas_quiz, pergunta_atual, perguntas_feitas
    
    perguntas_quiz = [
        {"pergunta": "Quem é o capitão atual da FURIA?", "resposta": "yuurih"},
        {"pergunta": "Em qual ano a FURIA alcançou a semifinal de um Major?", "resposta": "2020"},
        {"pergunta": "Qual é o nome completo do yuurih?", "resposta": "Yuri Santos"},
        {"pergunta": "Em qual jogo a FURIA é mais conhecida?", "resposta": "Counter-Strike"},
        {"pergunta": "Qual é a cor predominante do logo da FURIA?", "resposta": "preto"},
        {"pergunta": "Qual é o nome do jogador conhecido como 'professor'?", "resposta": "fallen"},
        {"pergunta": "Em qual continente a FURIA é baseada?", "resposta": "América do Sul"},
        {"pergunta": "Qual é o nome do treinador da FURIA?", "resposta": "sidde"},
        ]

    perguntas_disponiveis = [p for p in perguntas_quiz if p not in perguntas_feitas]
    
    if not perguntas_disponiveis:
        perguntas_feitas.clear()
        perguntas_disponiveis = perguntas_quiz

    pergunta_atual = random.choice(perguntas_disponiveis)
    perguntas_feitas.append(pergunta_atual)
    
    if len(perguntas_feitas) > MAX_PERGUNTAS_MEMORIA:
        perguntas_feitas.pop(0)
    
    user_states[call.message.chat.id] = pergunta_atual
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add("Enviar resposta")
    
    bot.send_message(call.message.chat.id, f"📝 {pergunta_atual['pergunta']}")

@bot.message_handler(func=lambda msg: True)
def tratar_resposta(msg):
    try:
        if msg.chat.id not in user_states:
            return

        pergunta_atual = user_states[msg.chat.id]
        if pergunta_atual["resposta"].lower() in msg.text.lower():
            bot.send_message(msg.chat.id, "✅ Resposta correta!")
        else:
            bot.send_message(msg.chat.id, f"❌ Resposta errada! A resposta correta era: {pergunta_atual['resposta']}")
        
        del user_states[msg.chat.id]
    except Exception as e:
        print(f"Erro ao tratar resposta: {e}")

    markup = types.InlineKeyboardMarkup()
    btn_jogos = types.InlineKeyboardButton("🎯 Próximos Jogos", callback_data="jogos")
    btn_noticias = types.InlineKeyboardButton("📰 Notícias", callback_data="noticias")
    btn_quiz = types.InlineKeyboardButton("🎮 Próxima Pergunta", callback_data="quiz")
    btn_redes_sociais = types.InlineKeyboardButton("🔗 Redes Sociais", callback_data="redes_sociais")
    markup.add(btn_jogos, btn_noticias, btn_quiz, btn_redes_sociais)
    
    bot.send_message(msg.chat.id, "Escolha uma opção:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "redes_sociais")
def redes_sociais(call):
    redes = """
    🔗 Redes sociais da FURIA:
    - Facebook: https://www.facebook.com/Furiagg
    - Twitter: https://twitter.com/Furia
    - Instagram: https://www.instagram.com/Furiagg
    - YouTube: https://www.youtube.com/Furiagg
    - TikTok: https://www.tiktok.com/@Furia
    """
    bot.send_message(call.message.chat.id, redes)

@bot.message_handler(func=lambda msg: True)
def handle_messages(message):
    try:
        pass
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        bot.reply_to(message, "Desculpe, ocorreu um erro ao processar sua mensagem.")

def iniciar_bot():
    while True:
        try:
            print("Bot iniciado! Pressione Ctrl+C para encerrar.")
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            print(f"Erro no polling: {str(e)}")
            time.sleep(10)  # Espera 10 segundos antes de tentar novamente

if __name__ == "__main__":
    iniciar_bot()
