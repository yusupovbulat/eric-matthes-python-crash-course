names = []
if len(names) == 0:
    print('We need to find some users!')
else:
    for name in names:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + name.title() + ', thank you for logging in again!')
