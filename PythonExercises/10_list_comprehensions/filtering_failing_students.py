# this ternary filters students that has less than 75
# also note that the names of students are formatted to ensure clean output
# this code block include unpacking of student list of tuple

students = [('john', 90), ('MARY', 72), ('aLiCe', 65), ('bob', 88), ('dave', 59)]
failing_students = [(name.title(), score) for name, score in students if score <= 75 ]
print(failing_students)