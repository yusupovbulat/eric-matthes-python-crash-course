pizzas = ['mozzarella', 'neapolitan', 'italy']
friend_pizzas = pizzas[:]
pizzas.append('four cheese')
friend_pizzas.append('diablo')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
