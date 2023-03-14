# Courses: colt_py_bootcamps 72

# Ask for age.
# 18 allowed to Connect
# 21 allowed to drink

age = input("How old are you: ")

# cant use, because it may have empty string 
# age = int(input("How old are you: "))

# if age != '':
if age:
    # best to cast at the beginning, safe in if-condition
    # age = int(age)
    if int(age) >= 18 and int(age) < 21:
        print("Enter with wrtistband")
    elif int(age) >=21:
        print("Can Drink")
    else:
        print("cant enter")
else:
    print("Please enter valid number")


""" No nesting solution
    if age and (int(age) >= 18 and int(age) < 21):
    elif age and (int(age) >=21): 
"""

# Refactored code: The following is the efficient way. 'Sift-through' approach
# Note: we dont need "and", because 'elif age >= 18' wiil true if previous-if-condition is false
if age:
    age = int(age)
    if age >= 21:
        print("Can Drink")
    elif age >=18:
        print("Enter with wrtistband")
    else:
        print("cant enter")
else:
    print("Please enter valid number")