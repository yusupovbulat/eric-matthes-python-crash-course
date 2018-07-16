people = {
        'zramazanova': {
            'first': 'zemfira',
            'last': 'ramazanova',
            'location': 'ufa',
            },
        'yushevshuk': {
            'first': 'yuri',
            'last': 'shevshuk',
            'location': 'ufa',
            },
        'aivan': {
            'first': 'ivan',
            'last': 'alekseev',
            'location': 'belgorod',
            },
        }
for nick, info in people.items():
    print('\nNickname: ' + nick)
    full_name = info['first'] + " " + info['last']
    location = info['location']
    print("\nFull name: " + full_name.title())
    print("\nLocation: " + location.title())
