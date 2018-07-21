def make_sandwich(*ingridients):
    print('\nMaking a sandwich with the following ingridients:')
    for ingridient in ingridients:
        print('- ' + ingridient)


make_sandwich('becon')
make_sandwich('cheese', 'green peppers')
make_sandwich('becon', 'cheese', 'green peppers')
