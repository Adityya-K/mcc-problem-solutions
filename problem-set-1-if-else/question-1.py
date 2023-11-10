# Problem 1: Write a program that finds the maximum of two numbers inputted by
# the user.

# Create two variables to store user input. We need to make sure to convert the
# variables to integers so that we can compare them later in the if statement.
# If we didn't convert to int the if statement would compare our inputs as
# strings which is not what we want.
a = int(input())
b = int(input())

# Write an if statement comparing the user inputted numbers
#
# If the user input a is greater than user input b
if a > b:
    # print the value of a to the console
    print(a)
# If a is not greater than b, that means b is greater than a
else:
    # print b out to the console to match the test case
    print(b)

# With this problem you could add a case where the inputs are equal however, it
# is not required by the question and is not needed for your solution to pass!
