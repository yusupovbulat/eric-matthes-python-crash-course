current_users = ['mike', 'fiona', 'david', 'bob', 'eric']
new_users = ['john', 'rick', 'eric', 'nick', 'bob']
for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print('Name ' + new_user.lower() + ' is used! Please enter new name!')
