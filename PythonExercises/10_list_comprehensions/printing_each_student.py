
students = [('john', 90), ('MARY', 72), ('aLiCe', 65), ('bob', 88), ('dave', 59)]
for name, score in students:        # unpacking the students list of tuple
    print(f"{name.title()} scored {score}")     # formatting the names of each student