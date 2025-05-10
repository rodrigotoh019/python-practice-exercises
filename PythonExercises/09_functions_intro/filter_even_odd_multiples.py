# this is interesting, the def code block filters the value and print even numbers that are divisible by 4

def filter_even_number(n):
    return [i for i in range(1, n + 1) if i % 2 == 0 and i % 4 !=0]
print(filter_even_number(10))

# nums = list(range(1, 21))
# evens = [n for n in nums if n % 2 == 0]
# odds = [n for n in nums if n % 2 != 0]
# multiples_of_3 = [n for n in nums if n % 3 == 0]
# print(nums)
# print(evens)
# print(odds)
# print(multiples_of_3)