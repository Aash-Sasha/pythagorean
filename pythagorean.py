# Import modules that operate math. Especially for square root, when I have done only import math, sqrt function did not work.
import math
from math import sqrt

# Explains the program. Also asks the person which side he wants to know of.
print """This is a program that can solve pythagorean triangles.
Which side do you want to solve for?
'a' = side 1
'b' = side 2
'c' = hypotenuse"""

# Gives the options
print "1. 'a'"
print "2. 'b'"
print "3. 'c'"

# Makes the person put the input
option = input("Type the option:\n1, 2, or 3\n> ")

# If-statement of the first option.
if option == 1:
    # They would input an integer so I put int.
    b = int(input("What is the length of side 2?\n> "))
    c = int(input("What is the length of the hypotenuse?\n> "))
    # Calculates the length of side 1. Sqrt is square root and pow is exponential power.
    print "The length of side 1 is ", sqrt(pow(c, 2) - pow(b, 2))

# If-statement of the second option.
elif option == 2:
    # Would input an integer.
    a = int(input("What is the length of side 1?\n> "))
    c = int(input("What is the length of the hypotenuse\n> "))
    #Calculates the length of side 2.
    print "The length of side 2 is ", sqrt(pow(c, 2) - pow(a, 2))

# If-statement of the third option.
elif option == 3:
    # Would input an integer.
    a = int(input("What is the length of side 1?\n> "))
    b = int(input("What is the length of side 2?\n> "))
    #Calculates the length of the hypotenuse.
    print "The length of the hypotenuse is ", sqrt(pow(a, 2) + pow(b, 2))
