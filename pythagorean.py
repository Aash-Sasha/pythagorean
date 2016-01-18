import math
from math import sqrt
from time import sleep

print """This is a program that can solve pythagorean triangles.
Which side do you want to solve for?
'a' = side 1
'b' = side 2
'c' = hypotenuse"""

print "1. 'a'"
print "2. 'b'"
print "3. 'c'"

option = input("Type the option:\n1, 2, or 3\n> ")

if option == 1:
    b = int(input("What is the length of side 2?\n> "))
    c = int(input("What is the length of the hypotenuse?\n> "))
    print "The length of side 1 is ", sqrt(pow(c, 2) - pow(b, 2))

elif option == 2:
    a = int(input("What is the length of side 1?\n> "))
    c = int(input("What is the length of the hypotenuse\n> "))
    print "The length of side 2 is ", sqrt(pow(c, 2) - pow(a, 2))

elif option == 3:
    a = int(input("What is the length of side 1?\n> "))
    b = int(input("What is the length of side 2?\n> "))
    print "The length of the hypotenuse is ", sqrt(pow(a, 2) + pow(b, 2))
