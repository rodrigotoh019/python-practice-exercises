# # CLI Shell - User interaction and menu routing
#
# while True:
#     prompt = input("Type 'Open' to access the menu and type 'Close' to quite:\n>").lower()
#
#     if prompt == "open":
#         break
#     elif prompt == "close":
#         exit()
#     else:
#         print("Invalid Input! Please choose between 'Open' or 'Close'.")
#
# while True:
#     print("\n=== Student Grade Analyzer Menu ===")
#     print("1. View All Students")
#     print("2. Add a Student")
#     print("3. Edit a Student")
#     print("4. Remove a Student")
#     print("5. Analyze Scores")
#     print("6. Exit")
#
#     choice = input("Choose an option (1 - 6):\n>")
#
#     if choice == "1":
#         def get_students_data(student_data):
#             student_info = []
#             for name, scores in student_data:
#                 student_avg = round(sum(scores) / len(scores), 2)
#                 student_dict = {
#                     'name': name,
#                     'scores': scores,
#                     'grades': [letter_grade_scale(score) for score in scores],
#                     'average': student_avg,
#                     'average_grade': letter_grade_scale(student_avg)
#                 }
#                 student_info.append(student_dict)
#             sorted_students = sorted(students_data, key=lambda x: x['name'])
#             return student_info, sorted_students
#         print
#
#     elif choice == "2":
#         # add_student()
#     elif choice == "3":
#         # edit_student()
#     elif choice == "4":
#         # remove_student()
#     elif choice == "5":
#         # analyze_score()
#     elif choice == "6":
#         print("Exiting The Program. Goodbye!")
#         break
#     else:
#         print("Invalid Option. Please select between 1 - 6.")


def double_number(number):
    result = number * 2
    return result
print(double_number(5))

def triple_number(number):
    return number * 3
print(triple_number(3))
result = triple_number(8)
print(result)


def add_five(number):
    return number + 5
result1 = add_five(5)
result2 = add_five(15)
print(result1)
print(result2)
print(result1 + result2)

def ww_ww(ww):
    return ww + 5
aa = ww_ww(1)
print(aa)
aa2 = int(aa)
print(aa2 + 2)
print(sum