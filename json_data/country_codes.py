from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    for country_code, name in COUNTRIES.items():
        if name == country_name:
            return country_code