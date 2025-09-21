# I've also done two code block for this exercise.
# The if statement does not repeat itself so you need to re-run it to try again

sports = ["basketball", "soccer", "tennis"]
guess = input("Enter a sport: ").lower()
if guess in sports:
    print("Correct!")
else:
    print("Try again")

# Or

sports = ("basketball", "volleyball", "football", "tennis")
while True:
    guess = input('Enter a sport:\t').lower()
    if guess in sports:
        print(f'{guess}')
        break
    else:
        print(f'Please select one of these {sports}')