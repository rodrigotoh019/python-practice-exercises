# two basic sample of zipping

names = ['Anna', 'Ben', 'Cara']
grades = [85, 92, 78]
students = tuple(zip(names, grades))    # Converts to tuple
print(students)


names = ["a", "b"]
scores = [1, 2, 3]
students = list(zip(names, scores))
print(students)  # Only two pairs created