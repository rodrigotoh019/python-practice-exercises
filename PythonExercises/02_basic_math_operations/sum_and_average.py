x = int(input(f'How many numbers do you want to enter? '))
numbers = []        # empty list to store user's input
for i in range(1, x + 1):
    numbers.append(float(input(f'Enter number #{i}: ')))
add = int(sum(numbers))     # type convertion
ave = add / len(numbers)    # using len to count how many values inside the list
print(f'Sum: {add}\nAverage: {ave:.1f}')