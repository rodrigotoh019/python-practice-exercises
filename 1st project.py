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
#     sport = input('Enter a sport:\t')
#     if sport in sports:
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

def analyze_score(m):
    print(f'hello {m}')
analyze_score('Rod')