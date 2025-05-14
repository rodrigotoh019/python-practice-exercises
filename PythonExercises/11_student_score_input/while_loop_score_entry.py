# this is a while loop that stores name and score and convert it into a tuple

students = []
while True:
    name = input("Enter student name (or 'done'): ")    # telling the user to input 'done' if finish
    if name.lower() == 'done':      # converts all user input into lowercase so that regardless if the user inputted 'DONE' or any format, it would still be registered as lowercased
        break       # if the user inputted 'done' then the program will stop
    score = float(input("Enter score: "))
    students.append((name.title(), score))      # formatting to ensure clean and organized names, converted into tuple to make it easier to unpack later on
print(students)