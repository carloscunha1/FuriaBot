🐍 FuriaBot
FuriaBot é um bot do Telegram desenvolvido em Python que utiliza Selenium para monitorar partidas da equipe FURIA e enviar notificações automaticamente. Ele foi criado para fornecer atualizações em tempo real sobre os jogos da FURIA, facilitando o acompanhamento para os fãs.

📁 Estrutura do Projeto
A estrutura de diretórios do projeto é a seguinte:

arduino
Copiar
Editar
FuriaBot/
├── bot.py
├── config.example.py
├── requirements.txt
├── scraping.py
└── README.md

bot.py: Script principal que inicializa o bot do Telegram e gerencia a lógica de envio de mensagens.

config.example.py: Arquivo de exemplo contendo as configurações necessárias, como tokens e IDs de chat. Deve ser renomeado para config.py e preenchido com suas informações.

requirements.txt: Lista de dependências do projeto que podem ser instaladas com pip.

scraping.py: Script responsável por realizar a automação com Selenium para extrair informações das partidas da FURIA.

⚙️ Configuração e Execução
1. Clonar o Repositório
Clone o repositório para sua máquina local:

bash
Copiar
Editar
git clone https://github.com/carloscunha1/FuriaBot.git
cd FuriaBot
2. Instalar Dependências
Instale as dependências necessárias utilizando o pip:

bash
Copiar
Editar
pip install -r requirements.txt
3. Configurar o Bot do Telegram
Crie um novo bot no Telegram utilizando o BotFather e obtenha o token de acesso.

Copie o arquivo config.example.py para config.py:

bash
Copiar
Editar
cp config.example.py config.py
Edite o arquivo config.py e insira o token do seu bot e o ID do chat onde as notificações serão enviadas.

4. Executar o Bot
Inicie o bot executando o script principal:

bash
Copiar
Editar
python bot.py
O bot começará a monitorar as partidas da FURIA e enviará notificações para o chat configurado.

🧪 Desenvolvimento com Selenium
O FuriaBot utiliza o Selenium para automatizar a navegação em sites que contêm informações sobre as partidas da FURIA. O script scraping.py é responsável por:

Acessar páginas específicas que listam as partidas da FURIA.

Extrair informações relevantes, como data, adversário e resultado da partida.

Retornar essas informações para que o bot.py possa processá-las e enviar notificações.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, correções ou novas funcionalidades.

📄 Licença
Este projeto está licenciado sob a MIT License.
