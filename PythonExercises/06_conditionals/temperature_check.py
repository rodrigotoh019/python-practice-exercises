# Conditional logics

# temperature = int(input('What is the temperature? '))
# print(f'Today is a {'Hot Day' if temperature >=33 else 'Cold day'}')

# Or

# for multi-conditional logic

temperature = int(input('What is the temperature? '))
if temperature >=30:
    print('Today is a hot day')
elif 26 < temperature < 30:
    print('Today is a good day!')
else:
    print('Today is a cold day')

# You can also do one-line ternary for multi-conditional logic but the readability would be a problem


