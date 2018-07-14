guests_list = ['albert', 'nikita', 'ruslan', 'rashid']
message1 = 'Dear ' + guests_list[0].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message2 = 'Dear ' + guests_list[1].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message3 = 'Dear ' + guests_list[2].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message4 = 'Dear ' + guests_list[3].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
print(message1)
print(message2)
print(message3)
print(message4)

missing_guest = guests_list.pop(3)
print(missing_guest.title() + ' can not come')
guests_list.insert(3, 'david')
message1 = 'Dear ' + guests_list[0].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message2 = 'Dear ' + guests_list[1].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message3 = 'Dear ' + guests_list[2].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
message4 = 'Dear ' + guests_list[3].title() + '! I invite you to dinner tomorrow at 3 p.m.' 
print(message1)
print(message2)
print(message3)
print(message4)

