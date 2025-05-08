# another if-else statement with len

name = input('Please enter your name: ')
if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name must be less than 50 characters')
else:
    print('Name looks good!')