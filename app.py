from asyncio import TimerHandle
from itertools import product
from multiprocessing.spawn import old_main_modules
from pickle import NEWOBJ_EX
from xml.sax.saxutils import prepare_input_source
import math

# Feb 27, 2025

# print('Rigo Toh')
# print('o-----')
# print(' | | | |')
# print('*' * 10)
# The * is a multiplication of the value inside the '', in this case the *
# price = 10
# rating = 4.9
# is_published = False
# print(price)

# We check in a patient named John Smith. He's 20 years old and is a new patient.

# name = 'John Smith'
# str = name
# age = 20
# int = age
# is_new = True
# str = is_new
# print (name, age, is_new)

# name = input('What''s your name? ')
# print('Hi ' + name)

# Ask two questions: person's name and favourite color. Then, print a message like "Mosh likes blue"

# name = input("What's your name? ")
# print('Hi ' + name)
# color = input('What about your favourite color? ')
# print('So you like ' + color)
# print(name + ' likes the color ' + color)

# The set of codes I made for this exercise is meant to have sequence of questions. I'm initially looking for a set of code to do this in the internet without doing the exercise first. The tutorials I saw in google search are different from what I want, so I then just made this series of codes and see what would happen. I was surprised that the input() can automatically use in sequence question. Nice.


# Type conversion
# birth_year = input('Birth year: ')
# age = 2025 - int(birth_year)
# print(age)

#The type conversion here is the string or 'str' birth_year to integer or 'int'. This is needed to get the value of the code.

# Ask a user their weight (in pounds), convert it to kilograms and print on the terminal.

# weight_pounds = float(input('What''s your weight in pounds? '))
# pounds_to_kilo = 0.45359237 * weight_pounds
# print('Your weight in kilo is ' + str(pounds_to_kilo))

# I had quite a difficult time here. Firstly, I don't know what's the conversion of pounds to kilo, but that's an easy task, just a search away in google but then my brain can't comprehend at first how to put the conversion here. I know how to do it in my brain, but I can't put it into words, then I looked in the formula of conversion, so I now know how to put it here, but then I had an error because of the multiplication of the conversion. My weight in pounds is 198.41, and I converted the "weight_pounds" into int(), I thought it would run smoothly, but then I got an error again underlining the int(weight_pounds), I thought the "*" is the problem then I realized that I used a number value with decimal point which means the conversion must be str to float, not str to int. After running again, it runs smoothly now, so what I want to do after that is to give a prompt that says that the weight I input has been converted into kg and is *** so I tried print([prompt] + pounds_to_kilo), the pounds_to_kilo is an integer value so as expected after I ran it, I got an error underlining the pounds_to_kilo, and then I think of a way to convert that into a string. What I did at first is to just create a str(pounds_to_kilo) in the between the print and the pounds_to_kilo, but it still doesn't work, so I examined the prompt, and then I did the str(pound_to_kilo) inside the print value, and it worked!

# personal_info = {'Name': 'John Doe', 'Address': '123 Test Street, NY, 10000', "Phone": '123-456-7890', 'College Major': 'MBA'}
#
# print(f'Name: \t {personal_info['Name'].title()}')
# print(f'Address: {personal_info['Address'].title()}')
# print(f'Phone:\t {personal_info['Phone']}')
# print(f'Major:\t {personal_info['College Major']}')

# projected_total_sales = int(input('What''s the projected amount of total sales this year? : \t'))
# percent = 0.23 * projected_total_sales
# print(f'The 23% of the projected amount of {projected_total_sales} this year is : {percent}')

# price1 = float(input('Please enter the price for item 1: '))
# price2 = float(input('Please enter the price for item 2: '))
# price3 = float(input('Please enter the price for item 3: '))
# price4 = float(input('Please enter the price for item 4: '))
# price5 = float(input('Please enter the price for item 5: '))
# subtotal = price1 + price2 + price3 + price4 + price5
# sales_tax1 = 0.07 * subtotal
# total =  subtotal + sales_tax1
# print(f'The subtotal amount is ${subtotal:.2f}')
# print(f'Sales Tax (7%) of ${subtotal:.2f} is ${sales_tax1:.2f}')
# print(f'Total amount is ${total:.2f}')

# I know this is a primitive way to do this. I also know you can do this much easier if loop is used instead of input() but I don't know that as of writing so this will do! The process of what I did is so simple, you can deduce what I want to do lol


# x = int(input(f'How many numbers do you want to enter? '))
# numbers = []
# for i in range(1, x + 1):
#     numbers.append(float(input(f'Enter number #{i}: ')))
# add = int(sum(numbers))
# ave = add / len(numbers)
# print(f'Sum: {add}\nAverage: {ave:.1f}')

# num_items = 5			# Define the number of items
# prices = []				# Initialize an empty list to store item prices
# for i in range(1, num_items + 1):
#     price = float(input(f"Enter the price of item {i}: "))
#     prices.append(price)  		# Add the price to the list
# subtotal = sum(prices)  		# Adds all prices together
# sales_tax = subtotal * 0.07 		 # Calculates 7% tax
# total = subtotal + sales_tax
# print(f'Subtotal: {subtotal}\nAfter tax: {sales_tax}\nTotal: {total}')

# food = 3
# foods = []
# for i in range(1, food +1):
#     fav = input(f'Enter food #{i}: ')
#     foods.append(fav)
# print(f'Your favorite foods are:\n{'\n'.join(foods)}')

# n = int(input("How many numbers do you want to add? "))
# numbers = []
#
# for i in range(1, n + 1):
#     num = float(input(f'Enter number #{i}: '))
#     numbers.append(num)
#
# print(f'Sum: {sum(numbers)}')

# fist = 'ORigo'
# last = 'Toh'
# print(f'{fist[0]} [{last}] is a coder')
# print(fist.find('o'))

# is_good = False
# price = 1000000
# if is_good:
#     print('You need to put down 10%')
#     down = price * 0.1
# else:
#     print('You need to put down 20%')
#     down = price * 0.2
# print(f'It will be ${down:.2f}')

# characters = 50
# name = input('Please enter your name: ')
# if len(name) < 3:
#     print('Name must be at least 3 characters')
# elif len(name) > 50:
#     print('Name can be a maximum of 50 characters')
# else:
#     print('Name looks good!')

# your_weight = float(input('Weight: '))
# weight = input('(L)bs or (K)g: ')
# if your_weight is l or L:
#     weights = your_weight * 0.45359237
#     print(f'Your weight is {weights:.1f} pounds')
# else:
#     weights = your_weight * 2.2
#     print(f'Your weight is {weights:1.f} kilograms')

# Mali to sa taas, ito dapat:

# weight = float(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == 'L':
#     converted = weight * 0.45359237
#     print(f'You are {converted} kilos')
# else:
#     converted = weight / 0.45359237
#     print(f'You are {converted:.2f} pounds')

# Ganito dapat, sa unit kukuha ng ifelse tapos .upper ung sagot dun sa upper or lower case na isasagot ng user
# Ung weight na ilalagay ng user, sa convertion lang sya magagamit.

# z = int(input('How many: '))
# nums = []
# for i in range(1, z +1):
#     num = input(f'Enter #{i}: ')
#     nums.append(num)
# print(f'You have entered:\n{"\n".join(nums)} ')

# e = int(input('how many: '))
# num = []
# prod = 1
# for i in range(1, e +1):
#     nums = int(input(f'Enter #{i}: '))
#     num.append(nums)
#     prod = prod * num
# print(f'Product: {prod}')


# number = int(input('Enter the number: '))
# n = 0
# if n < number:
#     print('Positive')
# elif n > number:
#     print('Negative')
# else:
#     print('Zero')

# n = 5
# num = []
# for i in range(1, n +1):
#     numbers = int(input(f'Enter a number #{i}: '))
#     num.append(numbers)
# print(f'The largest number in the list is {max(num)}')

# first = int(input('Enter a number #1: '))
# second = int(input('Enter a number #2: '))
# if first > second:
#     print('The first number is greater than the second')
# elif first < second:
#     print('The second number is greater than the first')
# elif first == second:
#     print('Both numbers are equal')

# x = int(input('Enter a number: '))
# num = []
# for i in range(1, x +1):
#     numbers = int(input(f'Enter the #{i}: '))
#     num.append(numbers)
# print(f'Sum: {sum(num)}')

x = [('aa',22), ('bb',44), ('cc',55)]
s = []
sort_asc = sorted(x, key=lambda x: x[0])
print(sort_asc)

command = input("\nType 'menu' to open the Student Grade Analyzer or 'exit' to quit:\n> ").lower()
print(command)