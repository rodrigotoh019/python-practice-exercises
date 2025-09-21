# def function for checking temperature using if-else statement

def check_temp(temp):
    if temp > 30:
        return "Hot"
    elif temp < 15:
        return "Cold"
    return "Warm"       # it was placed here, else the if statement would error
print(check_temp(20))
