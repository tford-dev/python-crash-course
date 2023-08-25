def city_country(city, country):
    return f"{city.title()}, {country.title()}.";

def city_country_pop(city, country, population=""):
    if population != "":
         return f"{city.title()}, {country.title()} has a population of {int(population)}."
    else:
        return f"{city.title()}, {country.title()}.";
