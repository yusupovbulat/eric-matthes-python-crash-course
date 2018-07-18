sandwich_orders = ['pastrami', 'arepa', 'doner-kebab', 'pastrami',
        'vada paw', 'kacu-sando', 'pastrami', 'bokadilio', 'pastrami']

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('Pastrami is no more:')
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())
