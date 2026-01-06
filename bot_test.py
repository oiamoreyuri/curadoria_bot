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

from amazon_collector import get_sample_amazon_offers
from offer_rules import is_good_offer

if __name__ == "__main__":
    ofertas = get_sample_amazon_offers()

    for oferta in ofertas:
        if is_good_offer(oferta["old_price"], oferta["new_price"]):
            mensagem = (
                f"🔥 <b>OFERTA REAL</b>\n\n"
                f"{oferta['product']}\n"
                f"💰 De: R$ {oferta['old_price']:.2f}\n"
                f"➡️ Por: R$ {oferta['new_price']:.2f}\n\n"
                f"📦 {oferta['store']}"
            )
            enviar_mensagem(mensagem)


