# pounds to kilo converter

weight_pounds = float(input('What''s your weight in pounds? ')) # user's input automatically converted to float
pounds_to_kilo = 0.45359237 * weight_pounds                     # this is the pounds to kilo formula
print(f'Your weight in kilo is {pounds_to_kilo:.2f}')           # the :.2f is to format the float to only have 2 decimal
