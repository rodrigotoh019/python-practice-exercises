# Another ternary logic, this is to avoid unnecessary and repeating lines.

price = float(input('Enter total price: '))
if price >=500:
    discount = price * 0.10
else:
    discount = price * 0.05
total = price - discount
print(f'Discount: ${discount}\nTotal: ${total:.2f}')

# Or


price = float(input('Enter total price: '))
discount = price * (0.10 if price >=500 else 0.05)
total = price - discount
print(f'Discount: ${discount}\nTotal: ${total:.2f}')


