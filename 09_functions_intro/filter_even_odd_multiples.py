# this ternary def function filters a list so only even numbers remains
# then it further filters out the list so any number that is a multiple of 4 gets excluded

def filter_even_number(n):
    return [i for i in range(1, n + 1) if i % 2 == 0 and i % 4 !=0]
print(filter_even_number(10))

nums = list(range(1, 21))
evens = [n for n in nums if n % 2 == 0]     # even numbers formula
odds = [n for n in nums if n % 2 != 0]      # odd numbers formula
multiples_of_3 = [n for n in nums if n % 3 == 0]    # multiple of 3s formula
print(nums)
print(evens)
print(odds)
print(multiples_of_3)

# these are simple shorthands for basic math formulas