num_students = int(input('How many are the new Students:\t'))
students = []
passed_students = []
failed_students = []
for i in range(1, num_students+1):
    name = input(f"Enter the name of Student #{i}:\t")
    clean_name = name.title()
    while True:
        try:
            score = float(input(f'Score:\t'))
            if 0 <= score <= 100:
                students.append((clean_name, score))
                break
            elif score < 0:
                print("Score can't be negative")
            else:
                print('Please enter a score between 0 and 100.')
        except ValueError:
            print('Invalid Input! Please enter a numeric value.')
for name, score in students:
    clean_name = name.title()
    if score >= 70:
        passed_students.append((name.title(), score))
        print(f'{clean_name} passed with a score of {score:.2f}')
    elif score <= 70:
        failed_students.append((name.title(), score))
        print(f'{clean_name} failed with a score of {score:.2f}')

