# Use the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Use the sort() method with argument reverse=True
cars.sort(reverse=True)
print(cars)

# Use sorted() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list:')
print(cars)
print('\nHere is sorted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)

# Use sorted() method with argument reverse=True
print('\nHere is reversive sorted method:')
print(sorted(cars, reverse=True))

# Use method reverse(). This method only reverse list. DOES NOT SORT!
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list:')
print(cars)
print('\nHere is reversed list:')
cars.reverse()
print(cars)

# Use method len(). This method considers the length of the list(array).
print('\nCar list length:')
print(len(cars))

