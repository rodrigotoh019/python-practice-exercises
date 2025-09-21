# simple list printing

numbers = []
for _ in range(5):      # the _ means that the variable is irrelevant
    num = int(input("Enter a number: "))
    numbers.append(num)
print("You entered:", numbers)     # printing the list, tho it could be done with f-string