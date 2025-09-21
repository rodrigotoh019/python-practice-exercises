# simple listing of favorite foods with formatting

food = 3           # limiting it to three for small scale list
foods = []
for i in range(1, food +1):
    fav = input(f'Enter food #{i}: ')
    foods.append(fav)
print(f'Your favorite foods are:\n{'\n'.join(foods).title()}')

# \n.join() means each print would be at the new line
# .title() to ensure clean and nice format