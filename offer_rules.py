def is_good_offer(old_price: float, new_price: float) -> bool:
    """
    Avalia se uma oferta é boa o suficiente para ser publicada.
    Regra inicial: desconto mínimo de 20%.
    """
    if old_price <= 0:
        return False

    discount = (old_price - new_price) / old_price
    return discount >= 0.20
