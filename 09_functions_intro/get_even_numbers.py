# simple def functions to get even numbers with ternary logic
# both def function prints the same output, however the difference is how to tackle the filtration.

def get_evens(n):
    return [i for i in range(n+1) if i % 2 == 0]    # using even number formula
result = get_evens(10)
print(result)

# Or

def get_even_numbers(n):
    return [i for i in range(0, n+1, 2)]           # straight up filtering all even numbers
result = get_even_numbers(10)
print(result)