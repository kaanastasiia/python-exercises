def get_city_country(city, country, population=''):
    city_and_country=f"{city}, {country}{f' - population {population}' if population else ''}"
    return city_and_country.title()