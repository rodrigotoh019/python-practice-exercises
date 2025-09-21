import math
# sub = int(input('How many subjects do you have? '))
# subjects = []
# for i in range(1, sub +1):
#     subjects.append(f'Enter the grade for subject #{i}: ')
#     grade = int(input(f'Enter grade for {subjects}: '))
# print(f'Grade Report\n{subjects}: {grade}')
from idlelib.debugger_r import codetable
from re import Match

# sub = int(input('How many subjects do you have? '))
# grades = []
# subjects = []
# for i in range(1, sub +1):
#     subject = input(f'Enter subject #{i}: ')
#     subjects.append(subject)
#     grade = int(input(f'Enter grade for {subjects}: '))
#     grades.append(grade)
# print(f'Grade Report\n{subjects}: {grades}')

# Feeling ko kaya ko to isolve pero I'm pressed in time, so I need to move forward and would look into this after I have sufficient time/experience for easier solving

# x = 3.6
# print(math.floor(x))

# price = 1000000
# good_credit = False
#
# if good_credit:
#     print('You need to put down 10%')
#     down = (price * 0.10)
#     print(f'Your down payment will be ${down:.2f}')
# else:
#     print('You need to put down 20%')
#     down = price * 0.20
#     print(f'Your down payment will be ${down:.2f}')

# This is the standard if-else structure, we can lessen the lines with ternary operator

# price = 1000000
# good_credit = False
# down = price * (0.10 if good_credit else 0.20)
# print(f'You need to put down {10 if good_credit else 20}%')
# print(f'It will be ${down:.2f}')

# This is the ternary version for if-else structure. Simpler and cleaner than standard if-else structure

# num = int(input('Enter any number to test whether it is odd or even: '))
# if (num % 2) == 0:
#     print('The number is even')
# else:
#     print('The provided number is odd')

# num = int(input('Enter a number: '))
# print(f'Your number is {'Even' if (num % 2) == 0 else 'Odd'}')

# Both of the set of codes above are if-statement with the same function, to determine whether the number that the user inputted is either an odd or even number. The only difference is that the first set is a standard if-structure and the second one is the ternary version.

# age = int(input('Enter your age: '))
# print(f'You are an {'Adult' if age >=18 else 'Minor'}')

# This set determines if the user is an Adult or a Minor

# total_price = int(input('Enter total price: '))
# discount = total_price * (0.10 if total_price >=500 else 0.05)
# total = total_price - discount
# print(f'Final Price: ${total:.1f}')

# This set determines the final price after discount

# temperature = int(input('What is the temperature? '))
# print(f'Today is a {'Hot Day' if temperature >=30 else 'Cool Day'}')

# This checks the temperature but without the scales C or F, this is just a program that will tell if the value exceeds the set parameter or not

# username = input('Enter a username: ')
# length = len(username)
# print(f'{'Valid Username' if length >=5 else 'Too Short'}')

# I like this one because I integrated len() in an actual program that works! At first, I thought this set would not read numbers in the username, so I converted the input to int and float first, but I always get an error because it's a string, so I tried to just let it be and put a number in the username then it actually counted the numbers along with the letters, so cool!

# months = ("January", "February", "March", "April")
# march = months.index(2)
# print(march)

# animals = ("cat", "dog", "rabbit", "dog", "horse")
# print(animals[-3][0])

# fruits = int(input('How many favorite fruits you have?: '))
# fav = []
# for i in range(1, fruits + 1):
#     top_three = input(f'Enter your favorite fruits #{i}:\t')
#     fav.append(top_three)
# t = tuple(fav)
# print(fav)

# cities = ["Manila", "Cebu", "Davao", "Baguio"]
# print(f'• {cities[1]}\n• {cities[-1]}')


# sports = ("basketball", "volleyball", "football", "tennis")
# while True:
#     guess = input('Enter a sport:\t')
#     if guess in sports:
#         print(f'{sport}')
#         break
#     else:
#         print(f'Please select one of these {sports}')

# letters = ("a", "b", "c", "a", "d", "a", "e")
# print(letters.count("a"))

# Counting how many an element inside a tuple

# numbers = (10, 20, 30, 40, 50, 60, 70)
# print(numbers[:4])
#
# printing elements using slicing ":"

# def greet(name):
#     print(f'Hello, welcome {name}!')
# greet("Bibi")

# def add(a, b):
#     return a + b
# result = add(1, 2)
# print(result)

# def multiply(a, b):
#     return a * b
# print(multiply(4, 5))

# def get_min_max():
#     return [3, 7, 2, 9, 5]
# min_num = min(get_min_max())
# max_num = max(get_min_max())
# print(min_num)
# print(max_num)

# def get_even_numbers(n):
#     return [i for i in range(0, n+1, 2)]
# result = get_even_numbers(10)
# print(result)

# def check_temp(temp):
#     if temp > 30:
#         return "Hot"
#     elif temp < 15:
#         return "Cold"
#     else:
#         return "Warm"
# print(check_temp(20))


# def square_list(n):
#     return [i ** 2 for i in range(1, n+1)]
# print(square_list(5))

# def cube_list(n):
#     return [i ** 3 for i in range(1, n+1)]
# print(cube_list(4))

# def filter_even_number(n):
#     return [i for i in range(1, n + 1) if i % 2 == 0 and i % 4 !=0]
# print(filter_even_number(10))

# def filter_even(n):
#     result = []
#     for i in range(1, n + 1):
#         if i % 2 == 0 and i % 4 != 0:
#             result.append(i)
#     return result
# print(filter_even(10))

# Both versions print the same principle, list of even numbers but exclude the ones divisible by 4

# def filter_odd_squares(n):
#     return [i ** 2 for i in range(1, n +1) if i % 1 == 0 and i % 2 != 0]
# print(filter_odd_squares(5))

# The premise here is to get squared odd numbers without the even numbers, I used i ** 2 here because square = to the 2nd power

# def filter_multiples_of_3(n):
#     return [i ** 2 for i in range(1, n + 1) if i % 3 == 0]
# print(filter_multiples_of_3(10))

# square by 3s

# names = ['Anna', 'Ben', 'Cara']
# grades = [85, 92, 78]
# students = tuple(zip(names, grades))
# print(students)

# names = ['Alice', 'Bob', 'Charlie']
# scores = [90, 80, 95]
# students = (
#     (names[0], scores[0]),
#     (names[1], scores[1]),
#     (names[2], scores[2])
# )
# print(students)

# print((names[0], scores[0]), (names[1], scores[1]))


# x = int(input('Etneb:\t'))
# n = int(input('benta:\t'))
# print(x * n)


# students = []
# done = input('Type "done" if finished')
# while True:
#     name = input("Student's name: ").lower()
#     if name == 'done':
#         break
#     score = int(input("Score: "))
#     students.append((name, score))
# print(f'{students}')

# I had a problem with this because the output will also be lowercase instead of .title(), and at this time, I don't know how to insert the .title() before print

# students = []
#
# while True:
#     name_input = input("Student's name: ")


#     if name_input.lower() == 'done':  # Only convert for the check
#         break
#     name = name_input.title()  # Format the name properly for storing
#     score = int(input("Score: "))
#     students.append((name, score))

# Here's the correct way to handle my problem at that time. The .lower() in if statement is to check if the input value was the 'done', if not, it will then be stored inside the student list, and the creation of 'name' variable to convert the 'name_input' value to .title() is just to ensure that no matter how the user inputted the names of the students, the output will always be .title()

# students = [('john', 90), ('mary', 85)]
# cleaned_students = [(name.title(), score) for name, score in students]
# print(cleaned_students)

# This is a list of tuples list comprehended clean-up technique.

# students = [('john', 90), ('MARY', 72), ('aLiCe', 65), ('bob', 88), ('dave', 59)]
# failing_students = [(name.title(), score) for name, score in students if score <= 75 ]
# print(failing_students)


# formatted_students = [(name.title(), score) for name, score in students if name.lower() == 'done' break]
# print(formatted_students)

# grades = [88, 45, 76, 95, 63, 82, 55]
# passing_grades = []
# for passing in grades:
#     if passing >= 70:
#         passing_grades.append(passing)
# print(passing_grades)

# passing_grades = (passing for passing in grades if passing >= 70)
# print(passing_grades)
#
# passing_grades = [
#     (passing)
#     for passing in grades
#     if passing >= 70
# ]
# print(passing_grades)


# students = [('john', 90), ('MARY', 72), ('aLiCe', 65), ('bob', 88), ('dave', 59)]
# nice_name = [(name.title(), score) for name, score in students]
# print(nice_name)

# students = [('john', 90), ('MARY', 72), ('aLiCe', 65), ('bob', 88), ('dave', 59)]
# nice_name = []
# for name, score in students:
#     clean_name = name.title()
#     print(f'{clean_name} has a {score}')
#     nice_name.append((clean_name, score))

# students = [('JOE', 95), ('susan', 84), ('kevin', 68), ('lisa', 91), ('TOM', 72)]
# honor_students = []
# for name, score in students:
#     clean_name = name.title()
#     if score >= 85:
#         honor_students.append((clean_name, score))
#         print(f'{clean_name} is an honor student with a score of {score}')

# students = [('alex', 54), ('BEN', 73), ('Carla', 88), ('DANIEL', 42), ('Eva', 59)]
# failed_students = []
# for name, score in students:
#     clean_name = name.title()
#     if score <= 60:
#         failed_students.append((clean_name, score))
#         print(f'{clean_name} failed with a score of {score}')

# students = [('karen', 81), ('JACK', 67), ('tIna', 90), ('mark', 74), ('LUCY', 59)]
# passed_students = []
# failed_students = []
# for name, score in students:
#     clean_name = name.title()
#     if score >= 70:
#         passed_students.append((clean_name, score))
#         print(f'{clean_name} passed with a score of {score}')
#     elif score <= 70:
#         failed_students.append((clean_name, score))
#         print(f'{clean_name} failed with a score of {score}')
#     # or
#     else:
#         failed_students.append((clean_name, score))
#         print(f'{clean_name} failed with a score of {score}')

# def analyze_score(m):
#     print(f'hello {m}')
# analyze_score('Rod')

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
# print('Name: \t\t' + personal_info['Name'].title())

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

# num = 3
# numbers = []
# x = int(input(f'How many numbers do you want to enter? '))
# for i in range(1, num + 1):
#     inp = float(input(f'Enter number #{i}: '))
#     numbers.append(inp)
# add = int(sum(numbers))
# ave = add / 3
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
#     converted = weight * 0.45
#     print(f'You are {converted} kilos')
# else:
#     converted = weight * 2.2
#     print(f'You are {converted} pounds')

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
#     prod = prod * i
# print(f'Product: {prod * num}')


# number = int(input('Enter the number: '))
# n = 0
# if n < number:
#     print('Positive')
# elif n > number:
#     print('Negative')
# else:
#     print('Zero')

# n = 2
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

