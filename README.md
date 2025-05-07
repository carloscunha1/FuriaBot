---

# 🐍 FuriaBot

**FuriaBot** é um bot do Telegram desenvolvido em **Python** que utiliza **Selenium** para monitorar partidas da equipe **FURIA** e enviar notificações automaticamente.
Ele foi criado para fornecer atualizações em tempo real sobre os jogos da FURIA, facilitando o acompanhamento para os fãs.

---

## 📁 Estrutura do Projeto

A estrutura de diretórios do projeto é a seguinte:

```
FuriaBot/
├── bot.py                # Inicializa o bot e gerencia o envio de mensagens
├── config.example.py     # Exemplo de configurações (deve ser renomeado para config.py)
├── requirements.txt      # Dependências do projeto
├── scraping.py           # Automação com Selenium
└── README.md             # Este arquivo
```

---

## ⚙️ Configuração e Execução

### 1. Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/carloscunha1/FuriaBot.git
cd FuriaBot
```

### 2. Instalar Dependências

Instale os pacotes necessários com o `pip`:

```bash
pip install -r requirements.txt
```

### 3. Configurar o Bot do Telegram

* Crie um novo bot no Telegram usando o [BotFather](https://t.me/botfather) e obtenha o token.
* Copie o arquivo de exemplo:

```bash
cp config.example.py config.py
```

* Edite o `config.py` com:

  * `TOKEN`: o token do seu bot
  * `CHAT_ID`: o ID do chat onde as notificações serão enviadas

### 4. Executar o Bot

Inicie o bot com:

```bash
python bot.py
```

O bot começará a monitorar as partidas da FURIA e enviará mensagens no chat configurado.

---

## 🧪 Desenvolvimento com Selenium

O FuriaBot usa **Selenium** para automatizar a extração de dados em sites que exibem as partidas da FURIA.
O script `scraping.py` é responsável por:

* Acessar páginas com jogos da FURIA
* Extrair informações como:

  * Data
  * Adversário
  * Resultado
* Retornar essas informações para o `bot.py`, que processa e envia as mensagens

---

## 🤝 Contribuição

Contribuições são bem-vindas!
Sinta-se à vontade para abrir **issues** ou enviar **pull requests** com correções, melhorias ou novas funcionalidades.

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

Se quiser, posso gerar o `README.md` com esse conteúdo e o arquivo `LICENSE` com a MIT License prontos para adicionar ao seu repositório. Deseja isso?
