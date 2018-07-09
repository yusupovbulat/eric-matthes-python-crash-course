guests_list = ['albert', 'nikita', 'ruslan', 'rashid']
print((str)(len(guests_list)) + ' guest invited.')
message1 = 'Dear ' + guests_list[0].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message2 = 'Dear ' + guests_list[1].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message3 = 'Dear ' + guests_list[2].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message4 = 'Dear ' + guests_list[3].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
print(message1)
print(message2)
print(message3)
print(message4)
print()
print('Expand the guest list!')
print()
guests_list.insert(0, 'oleg')
guests_list.insert(3, 'valera')
guests_list.append('roman')

print((str)(len(guests_list)) + ' guest invited.')
message1 = 'Dear ' + guests_list[0].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message2 = 'Dear ' + guests_list[1].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message3 = 'Dear ' + guests_list[2].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message4 = 'Dear ' + guests_list[3].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message5 = 'Dear ' + guests_list[4].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message6 = 'Dear ' + guests_list[5].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message7 = 'Dear ' + guests_list[6].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message7)
print()
print('Reduce the guests list! Only two guests can come!')
print()
missing_guest = guests_list.pop(-1)
print('Dear ' + missing_guest.title() + '! I regret the cancellation of the invitation. Sorry!')
missing_guest = guests_list.pop(-1)
print('Dear ' + missing_guest.title() + '! I regret the cancellation of the invitation. Sorry!')
missing_guest = guests_list.pop(-1)
print('Dear ' + missing_guest.title() + '! I regret the cancellation of the invitation. Sorry!')
missing_guest = guests_list.pop(-1)
print('Dear ' + missing_guest.title() + '! I regret the cancellation of the invitation. Sorry!')
missing_guest = guests_list.pop(-1)
print('Dear ' + missing_guest.title() + '! I regret the cancellation of the invitation. Sorry!')
print()
print((str)(len(guests_list)) + ' guest invited.')
print()
print('Dear ' + guests_list[0].title() + '! The invitation remains in force. Waiting for you at 3 pm!')
print('Dear ' + guests_list[1].title() + '! The invitation remains in force. Waiting for you at 3 pm!')
print()
del guests_list[1]
del guests_list[0]
print(guests_list)

