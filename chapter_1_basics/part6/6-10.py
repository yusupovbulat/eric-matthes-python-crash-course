friends_favorite_numbers = {
        'ivan': [12, 54, 34],
        'petr': [43, 34, 65],
        'oleg': [3, 54, 1],
        }
for name, numbers in friends_favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are: " )
    for number in numbers:
        print(number)
