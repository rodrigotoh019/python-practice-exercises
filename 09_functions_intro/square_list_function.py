# these two def functions have basically the same function
# the main difference is that the former uses range, while the latter uses a list

def square_list(n):
    return [i ** 2 for i in range(1, n+1)]  # creates a range based on variable n
print(square_list(5))


def square_list(lst):
    return [x ** 2 for x in lst]
print(square_list([1, 5, 6, 10]))       # takes list as input
