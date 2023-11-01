# This function checks if a given year is a leap year in the Gregorian calendar.
def is_leap(year):
    # A year is a leap year if it's divisible by 4, except for years divisible by 100, which are not leap years,
    # unless they are also divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input a year from the user.
year = int(input("Enter a year: "))

# Print the result of the leap year check.
print(is_leap(year))
