def make_pizza(size, *toppings):
    """Вывод описание пиццы"""
    print('\nMaking a ' + str(size) +
          '-inch pizza with the follwing toppings:')
    for topping in toppings:
        print('- ' + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
