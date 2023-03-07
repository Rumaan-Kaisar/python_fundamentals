# Courses: colt_py_bootcamps 59
""" 
    User Input
        Python 3.6 uses the input() method.
        
        Python 2.7 uses the raw_input() method. 

        Note: User inputted values are in string data-type
"""

username = input("Enter username:")
print("Username is: " + username)

kms = input("How many kilometers did you cycle today?") #get user input

# Note: User inputted values are in string data-type 

miles = float(kms)/1.60934 # convert from string to float and divide
miles = round(miles, 2) #round the result
print(f"Your {kms}km ride was {miles}mi ")  

# ROUND SYNTAX:
# round(thing to round, how many decimal points)


