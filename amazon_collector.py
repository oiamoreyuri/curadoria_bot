import requests
from bs4 import BeautifulSoup

AMAZON_DEALS_URL = "https://www.amazon.com.br/gp/goldbox"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

def get_amazon_offers(limit: int = 5):
    """
    Coleta ofertas da página de Ofertas do Dia da Amazon.
    Versão segura: leitura simples de HTML público.
    """
    response = requests.get(AMAZON_DEALS_URL, headers=HEADERS, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    offers = []

    for item in soup.select("div[data-testid='deal-card']")[:limit]:
        title_tag = item.select_one("span.a-size-base-plus")
        price_tag = item.select_one("span.a-price-whole")
        old_price_tag = item.select_one("span.a-text-price span.a-offscreen")

        if not title_tag or not price_tag:
            continue

        try:
            new_price = float(
                price_tag.text.replace(".", "").replace(",", ".")
            )
            old_price = (
                float(
                    old_price_tag.text
                    .replace("R$", "")
                    .replace(".", "")
                    .replace(",", ".")
                )
                if old_price_tag else new_price
            )
        except ValueError:
            continue

        offers.append({
            "product": title_tag.text.strip(),
            "old_price": old_price,
            "new_price": new_price,
            "store": "Amazon"
        })

    return offers
