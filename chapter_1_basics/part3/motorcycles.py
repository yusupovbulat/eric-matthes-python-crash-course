# Create new array and print
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Add new element to array's last position with append() method
motorcycles.append('ducati')
print(motorcycles)

# Create empty array and add elements with append() method
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Add new element to array in selected position with insert() method
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Remove selected element from array
del motorcycles[-1]
print(motorcycles)

# Extract an element from an array and subsequent use with pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Example of use 1
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.')

# Example of use 2
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Remove an element from an array by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

