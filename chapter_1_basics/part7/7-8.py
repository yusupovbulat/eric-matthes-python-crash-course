sandwich_orders = ['arepa', 'doner-kebab', 'vada paw', 'kacu-sando', 'bokadilio']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your ' + current_sandwich + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

print('All cooked sandwiches:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
