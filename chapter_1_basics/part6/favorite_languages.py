favorite_laguages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

for name, lang in favorite_laguages.items():
    print(name.title() + "'s favorite language is " + lang.title() + ".")

for name in favorite_laguages.keys():
    print(name.title())

frinds = ['phil', 'sarah']
for name in favorite_laguages.keys():
    print(name.title())
    if name in frinds:
        print(" Hi " + name.title() + ", I see you favorite language is " +
              favorite_laguages[name].title() + "!")
print()
favorite_laguages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
for name in sorted(favorite_laguages.keys()):
    print(name.title() + ", thank you for talking the poll.")

print()
favorite_laguages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
print('The following languages have been mentioned:')
for language in favorite_laguages.values():
    print(language.title())
