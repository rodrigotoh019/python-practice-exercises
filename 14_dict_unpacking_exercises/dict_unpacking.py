students = {
    "Carl": [11,70,29,90],
    "Pen": [80,90,22,59],
    "Charlie": [88, 87, 91, 90]
}

# for name, scores in students.items():
#         print(name, *scores)              # printing with * to unpack individual value inside scores for each name

# for name, scores in students.items():     # printing the key, path with some formatting
#     print(name)
#     for score in scores:                  # for each name, unpack the scores further into individual value
#         print(" -", score)                # " -" is there to have some format on scores when printing

# for name, scores in students.items():
#     print(f"{name}, {sum(scores)/len(scores)}")   # getting the average score of each students

# student_list = [(name, sum(scores)/len(scores)) for name, scores in students.items()]     # list comprehension of the average score of students
# print(student_list)