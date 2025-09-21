# used to get the user's input or answer

name = input("What's your name? ") # asking the user "What's your name"
print('Hi ' + name)                # printing before another input prompt
color = input('What about your favourite color? ')
print('So you like ' + color)      # after getting the user input, both this
print(name + ' likes the color ' + color)   # and this will print successively

# As a beginner, this is okay. Alternately, you can do this with an f-string

print(f'Hi {name}')
print(f'So you like {color}')
print(f'{name} likes the color {color}')

# this will ensure clear output without messy string concatenation
