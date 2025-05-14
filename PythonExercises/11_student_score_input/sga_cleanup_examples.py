# this is a basic structure of what I want in my Student Grade Analyzer

students = [('karen', 81), ('JACK', 67), ('tIna', 90), ('mark', 74), ('LUCY', 59)]
passed_students = []
failed_students = []
for name, score in students:
    clean_name = name.title()
    if score >= 70:
        passed_students.append((clean_name, score))
        print(f'{clean_name} passed with a score of {score}')
    elif score <= 70:
        failed_students.append((clean_name, score))
        print(f'{clean_name} failed with a score of {score}')

    # or

    else:
        failed_students.append((clean_name, score))
        print(f'{clean_name} failed with a score of {score}')

# or

passed = [(n, s) for n, s in students if s >= 75]
failed = [(n, s) for n, s in students if s < 75]
print("Passed:", passed)
print("Failed:", failed)