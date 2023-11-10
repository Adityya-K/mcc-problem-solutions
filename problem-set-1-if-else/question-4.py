# Problem 4: Write a program that asks the user to input three sides of a
# triangle and then checks if the those three sides can form a valid triangle
#
# Let's first ask the user for three sides in the form of three inputs. We
# need to make sure that we convert each input to an integer to compare it.
a = int(input())
b = int(input())
c = int(input())

# Now we write an if statement that checks if the three inputs satisfy the
# triangle inequality theorum (i.e. the sum of any two sides is greater than
# the third)!
if a + b > c and a + c > b and b + c > a:
    # if the statement evalutes to true the triangle does exist and we output
    # that to the user
    print("Exists!")
# if the statement is not true
else:
    # the triangle does not exist and we output that to the user
    print("Does not Exist!")
