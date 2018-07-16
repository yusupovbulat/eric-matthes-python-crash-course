cities = {
        'ufa': {
            'country': 'russia',
            'population': 1115560,
            'fact': 'here was born Zemfira, Shevshuk and Tem Bulatov',
            },
        'reykjavik': {
            'country': 'iceland',
            'population': 126100,
            'fact': 'It is largest city in this country.',
            },
        'vancouver': {
            'country': 'canada',
            'population': 631486,
            'fact': 'Top five of worldwide cities for livability and quality of life.',
            },
        }
for city, info in cities.items():
    print("\nCity: " + city.title())
    country = info['country']
    fact = info['fact']
    print("Country: " + country.title())
    print("Fact about " + city.title() + ": " + fact)
