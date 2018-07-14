pizzas = ['mozzarella', 'neapolitan', 'italy', 'diablo', 'four cheese']
print('The first three items in the list are:') 
for pizza in pizzas[:3]:
    print(pizza.title())

print('\nThree items from the middle of the list are:')
for pizza in pizzas[1:4]:
    print(pizza.title())

print('\nThe last three items in the list are:')
for pizza in pizzas[2:]:
    print(pizza.title())
