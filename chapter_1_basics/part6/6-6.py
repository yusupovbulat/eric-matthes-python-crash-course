favorite_laguages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

names = ['bob', 'phil', 'lili', 'jen', 'tom']

for name in names:
    if name not in favorite_laguages.keys():
        print(name.title() + ', please take our poll!')
    else:
        print(name.title() + ', thank you for talking the poll.')
