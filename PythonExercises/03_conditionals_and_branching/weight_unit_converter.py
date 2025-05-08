# one of my first if-else statements

weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45359237     # pounds to kilo formula
    print(f'You are {converted:.2f} kilos')
else:
    converted = weight / 0.45359237     # kilo to pounds formula
    print(f'You are {converted:.2f} pounds')