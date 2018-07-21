def make_car(producer, model, **other_args):
    options = {}
    options['producer'] = producer
    options['model'] = model
    for key, value in other_args.items():
        options[key] = value
    return options


car = make_car('lada', 'vesta', color='grey', equipment='extra')
print(car)

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
