# this is one of my most early simple, basic project.
# it's a price calculator with subtotal, sales tax computation, and grand total

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

# looking back at my comment, I already know I can improve this with a loop and input, although I still don't know how at that time
# here's a better version of this price calculator

items = int(input('How many items: '))  # user defining how many items they have
prices = []                             # an empty list for storing the prices of each item
for i in range(1, items + 1):           # for loop, (1, items + 1) means that the counting starts at 1, stops at what number the user inputted in items, the + 1 is the number of increment each step of the loop
    prices.append(float(input(f'Price item #{i}: ')))   # the {i} refers to the i in for loop, it serves as the placeholder for the counter of the loop
subtotal = sum(prices)                  # sum(prices) means adding all the value inside the prices list
sales_tax = 0.07 * subtotal             # 7% tax formula
grand_total = subtotal + sales_tax
print(f'Subtotal: ${subtotal}')
print(f'Sale Tax (7%) of ${subtotal} is ${sales_tax:.2f}')
print(f'Grand Total: ${grand_total:.2f}')

# this is assuming that all the user will enter the right input without error
# I can still improve this with while loop and try-except, but as this is just a simple project, I'll leave it like that