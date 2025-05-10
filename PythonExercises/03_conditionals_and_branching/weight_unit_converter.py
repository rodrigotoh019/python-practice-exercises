# I've done two code block for this program. Both are basic structures and can still be improved.

weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    print(f"You are {weight * 0.45:.2f} kilos")
else:
    print(f"You are {weight / 0.45:.2f} pounds")

# Or

weight = float(input('Weight: '))
while True:
    unit = input('(L)bs or (K)g: ')
    if unit.upper() == 'L':
        converted = weight * 0.45359237     # pounds to kilo formula
        print(f'You are {converted:.2f} kilos')
        break
    elif unit.upper() == 'K':
        converted = weight / 0.45359237     # kilo to pounds formula
        print(f'You are {converted:.2f} pounds')
        break
    else:
        print('Please choose only between (L) or (K)')
        continue