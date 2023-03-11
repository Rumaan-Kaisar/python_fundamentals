# Courses: colt_py_bootcamps 66

# ------------- Using Identity Operators    -------------
#         Identity operators are used to compare the objects, 

#         is 	        Returns True if both variables are the same object	            x is y	
#         is not	    Returns True if both variables are not the same object	        x is not y	

import string


x = 1

print(x is 1)   # true
print(x is 2)   # false


""" 
        Naturally FALSY things:
        Such as :
            Empty objects
            Empty string
            None
            0
        
        Everything else is truthy
"""


if 0: 
    print("YAY!")

if 1: 
    print("YAY?")

# any number other than 0 is truthy
if -9: 
    print("HMM?")

# any non-empty string is truthy
animal = input("Your Favorite animal :")
if animal:
    print(animal + "is my favorite too")
else:
    print("You didn't say anything!")