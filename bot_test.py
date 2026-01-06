# bot test file

import logging

logging.basicConfig(level=logging.INFO)

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

from amazon_collector import get_amazon_offers
from offer_rules import is_good_offer

if __name__ == "__main__":
    ofertas = get_amazon_offers(limit=5)
    logging.info(f"Ofertas coletadas: {len(ofertas)}")

    for oferta in ofertas:
        old_p = oferta["old_price"]
        new_p = oferta["new_price"]

        if old_p > 0:
            discount = (old_p - new_p) / old_p
        else:
            discount = 0

        logging.info(
            f"{oferta['product']} | old: {old_p} | new: {new_p} | discount: {discount:.2%}"
        )

        if is_good_offer(old_p, new_p):
            mensagem = (
                f"🔥 <b>OFERTA REAL</b>\n\n"
                f"{oferta['product']}\n"
                f"💰 De: R$ {old_p:.2f}\n"
                f"➡️ Por: R$ {new_p:.2f}\n\n"
                f"📦 {oferta['store']}"
            )
            enviar_mensagem(mensagem)




