import requests
from bs4 import BeautifulSoup

SEARCH_URL = (
    "https://www.amazon.com.br/s"
    "?k=cafeteira"
    "&rh=p_n_specials_match%3A21618178011"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9"
}

def get_amazon_offers(limit: int = 5):
    response = requests.get(SEARCH_URL, headers=HEADERS, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    offers = []

    for item in soup.select("div.s-result-item")[:limit * 2]:
        title = item.select_one("h2 span")
        price = item.select_one("span.a-price span.a-offscreen")

        if not title or not price:
            continue

        try:
            new_price = float(
                price.text.replace("R$", "").replace(".", "").replace(",", ".")
            )
        except ValueError:
            continue

        # Amazon muitas vezes não mostra preço antigo
        old_price = new_price * 1.15  # heurística de teste (15%)

        offers.append({
            "product": title.text.strip(),
            "old_price": round(old_price, 2),
            "new_price": new_price,
            "store": "Amazon"
        })

        if len(offers) >= limit:
            break

    return offers
