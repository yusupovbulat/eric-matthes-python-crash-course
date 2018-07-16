pets = {
        'sharik': {
            'type': 'dog',
            'owner': 'vasya',
            },
        'murzik': {
            'type': 'cat',
            'owner': 'petya',
            },
        'tuzik': {
            'type': 'dog',
            'owner': 'vanya',
            },
        }
for nick, info in pets.items():
    print('\nNickname: ' + nick)
    owner = info['owner']
    pet_type = info['type']
    print(owner.title() + ' is the owner of this ' + pet_type + '.')
