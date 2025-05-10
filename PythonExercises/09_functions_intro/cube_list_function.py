# same logic as square list, there are two def functions
# the first one is using a range and the second one uses a list

def cube_list(n):
    return [i ** 3 for i in range(1, n+1)]
print(cube_list(4))


def cube_list(lst):
    return [x ** 3 for x in lst]
print(cube_list([1, 3, 6, 10]))