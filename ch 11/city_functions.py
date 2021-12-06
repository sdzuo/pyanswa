#11-1
def city_country(city, country, population =''):

    if population:
          fcc = f"{city}, {country} - population {population}"
    else:
        fcc = f"{city}, {country}"
    return fcc.title()
