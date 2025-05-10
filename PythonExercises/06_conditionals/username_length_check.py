# this checks the length of the user input.

username = input('Please enter your username: ')
if len(username) < 3:
    print('Username must be at least 3 characters')
elif len(username) > 50:
    print('Username can be a maximum of 50 characters')
else:
    print('Username looks good!')