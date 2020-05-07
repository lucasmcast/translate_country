from .en_us import COUNTRIES_ENUS
from .pt_br import COUNTRIES_PTBR

def translate_en_to_pt(country_name):
    """Função faz a tradução do nome do pais de ingles para portugues-br"""
    country_pt = None

    for key, value in COUNTRIES_ENUS.items():
        country_name = country_name.lower()
        value = value.lower()
        if country_name == value:
            country_pt = COUNTRIES_PTBR[key]

    return country_pt