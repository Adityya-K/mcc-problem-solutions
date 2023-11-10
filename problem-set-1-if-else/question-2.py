# Problem 2: Write a program that checks if the letter is uppercase or not

# First lets take user input.
a = input()

# Let's use an if statement along with the isUpper() method to check if the
# user input is uppercase
#
# If the letter is uppercase
if a.isupper():
    # print that the letter is uppercase
    print("Uppercase")
# If the letter is not uppercase, that means it has to be lowercase
else:
    # print that the letter is lowercase
    print("Lowercase")
