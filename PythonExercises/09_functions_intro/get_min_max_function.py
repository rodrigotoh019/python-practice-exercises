# I already gave it a list to simplify things

def get_min_max():
    return [3, 7, 2, 9, 5]
min_num = min(get_min_max())
max_num = max(get_min_max())
print(min_num)
print(max_num)

# or this code block that includes user input

def get_min_max(n):
    return min(n), max(n)
num = []
numbers = int(input('How many numbers you want: '))
for i in range(1, numbers +1):
    num.append(int(input(f'Enter #{i}: ')))
min_value, max_value = get_min_max(num)
print('Min:', min_value)
print('Max:', max_value)