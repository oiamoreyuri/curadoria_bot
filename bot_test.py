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

from offer_rules import is_good_offer

if __name__ == "__main__":
    produto = "Cafeteira Elétrica Exemplo"
    preco_antigo = 299.90
    preco_novo = 199.90

    if is_good_offer(preco_antigo, preco_novo):
        mensagem = (
            f"🔥 <b>OFERTA REAL</b>\n\n"
            f"{produto}\n"
            f"💰 De: R$ {preco_antigo:.2f}\n"
            f"➡️ Por: R$ {preco_novo:.2f}\n\n"
            f"👉 Oferta aprovada automaticamente"
        )
        enviar_mensagem(mensagem)

