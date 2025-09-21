# Sample of dissecting and printing with format a dictionary

personal_info = {'Name': 'John Doe', 'Address': '123 Test Street, NY, 10000', "Phone": '123-456-7890', 'College Major': 'MBA'}

print(f'Name: \t {personal_info['Name'].title()}')      # print name, \t is meant to have tab after Name:
print(f'Address: {personal_info['Address'].title()}')   # the .title() ensures the first letter is capitalized
print(f'Phone:\t {personal_info['Phone']}')             # numbers doesn't need formating
print(f'Major:\t {personal_info['College Major'].upper()}')     # MBA is an acronym, .upper() is the right format

# the \t ensures the clean and neat output, but as Address is longer, it does not need an additional \t to align with others
# the college major here is already in big letter so .upper() is not really needed.
# I would still advise to use formats to ensure the intended format regardless of the original value's format