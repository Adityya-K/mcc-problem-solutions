# Problem 3: Write a program that returns the user’s letter grade based on they
# percentage they input.
# Percentage >= 90 : Grade A
# Percentage >= 80 : Grade B
# Percentage >= 70 : Grade C
# Percentage >= 60 : Grade D
# Percentage >= 40 : Grade E
# Percentage < 40 : Grade F

# Ask the user for an input, converting it to an int so that we can compare it
# as a number.
a = int(input())

# Now we create a bunch of if/elif statements to check through each of the
# conditions provided by the question
#
# If a is greater or equal to 90
if a >= 90:
    # print corresponding grade according to statements in the problem
    print("A")
# If a is not greater than 90 we check if it is greater than 80
elif a >= 80:
    # print corresponding grade according to statements in the problem
    print("B")
# If a is not greater than 80 we check if it is greater than 70
elif a >= 70:
    # print corresponding grade according to statements in the problem
    print("C")
# If a is not greater than 70 we check if it is greater than 60
elif a >= 60:
    # print corresponding grade according to statements in the problem
    print("D")
# If a is not greater than 60 we check if it is greater than 40
elif a >= 40:
    # print corresponding grade according to statements in the problem
    print("E")
# If a meets none of the previous statements, meaning it is less than 40
else:
    # print corresponding grade according to statements in the problem
    print("F")
