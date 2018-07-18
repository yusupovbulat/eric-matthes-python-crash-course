responses = {}

active = True

while active:
    name = input('\nWhat is your name? ')
    response = input('Where would you like to relax in vacation? ')

    responses[name] = response

    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        active = False

print('\nPoll results')
for name, response in responses.items():
    print(name + ' would like to relax in ' + response)
