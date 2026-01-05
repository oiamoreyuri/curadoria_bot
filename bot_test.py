# bot test file

import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": texto,
        "parse_mode": "HTML"
    }
    r = requests.post(url, data=payload)
    return r.json()

if __name__ == "__main__":
    mensagem = "🤖 <b>Teste OK</b>\n\nBot rodando via GitHub Actions."
    print(enviar_mensagem(mensagem))
