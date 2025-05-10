names = ['Anna', 'Ben', 'Cara']
grades = [85, 92, 78]
students = list(zip(names, grades))
# Or students = tuple(zip(names, grades)) to convert the list into a tuple
print(students)

# Or manual index pairing

names = ['Alice', 'Bob', 'Charlie']
scores = [90, 80, 95]
students = (
    (names[0], scores[0]),
    (names[1], scores[1]),
    (names[2], scores[2])
)
print(students)

print((names[0], scores[0]), (names[1], scores[1]))