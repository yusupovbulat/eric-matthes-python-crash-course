favorite_laguages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        }
for name, languages in favorite_laguages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    if len(languages) == 1:
        for language in languages:
            print("\n" + name.title() + "'s favorite language is " +
                language.title() + ".")
