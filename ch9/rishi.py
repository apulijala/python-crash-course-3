def convert_conuntires_to_upper(countries):
    upper_countries = []
    for country in countries:
        upper_countries.append(country.upper())
    
    return upper_countries

countries  = countries = ["india", "england", "france"]
upper_countries = convert_conuntires_to_upper(countries)
print(upper_countries)
    