# Create empty list for storage aliens.
aliens = []
# Создание 30 зеленых пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)
print('...')

# Выводим количество созданных пришельцев.
print('Total numbers of aliens: ' + str(len(aliens)))
