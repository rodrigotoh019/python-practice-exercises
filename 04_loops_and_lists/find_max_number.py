# finding the largest number inside the list

n = 5           # limiting it with 5 to ensure a small list
num = []
for i in range(1, n +1):
    numbers = int(input(f'Enter a number #{i}: '))
    num.append(numbers)
print(f'The largest number in the list is {max(num)}')    # directly using max() instead of manually finding the largest number