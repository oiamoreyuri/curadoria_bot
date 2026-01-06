import os

MIN_DISCOUNT = float(os.getenv("MIN_DISCOUNT", "0.20"))

def is_good_offer(old_price: float, new_price: float) -> bool:
    """
    Avalia se uma oferta é boa o suficiente para ser publicada.
    Critério: desconto mínimo configurável via variável de ambiente.
    """
    if old_price <= 0:
        return False

    discount = (old_price - new_price) / old_price
    return discount >= MIN_DISCOUNT
