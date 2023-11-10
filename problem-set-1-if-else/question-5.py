# Problem 5: Ask the user to input a year and tell the user if the year
# inputted is a leap year or not (For this problem a leap year is a multiple of
# 4, and if it is a multiple of 100, it must also be a multiple of 400).
#
# Ask the user for input and convert it to an int to be compared later
a = int(input())

# Check if the input is a multiple of 4 and not a multiple of 100 or just
# a multiple of 400. If the whole condition is true, the year is a leap
# year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    # Output that the year is a leap year
    print("Is a leap year!")
# If the condition is not true, that means the year is not a leap year
else:
    # Output that the year is not a leap year
    print("Is not a leap year!")
