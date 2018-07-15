rivers = {
        'amazonas': 'brasilia',
        'nile': 'egypt',
        'volga': 'russia',
        }
for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title())

print()

for river in rivers.keys():
    print(river.title())

print()

for river in rivers.values():
    print(river.title())
