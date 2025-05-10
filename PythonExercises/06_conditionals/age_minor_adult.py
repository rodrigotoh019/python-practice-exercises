# I'm starting to learn the ternary logic at this time so there are two sample.

age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Or

age = int(input('Enter your age: '))
print(f'You are an {'Adult' if age >=18 else 'Minor'}')