def greet_users(names):
    """Вывод простого приветствия для каждого пользователя в списке."""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usersnames = ['hannah', 'ty', 'margot']
greet_users(usersnames)
