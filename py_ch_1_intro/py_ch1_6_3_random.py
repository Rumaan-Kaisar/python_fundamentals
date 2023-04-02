# All from exercise
# NO TOUCHING PLEASE---------------
from random import randint
choice = randint(1,10)
# NO TOUCHING PLEASE---------------

# YOUR CODE GOES HERE:
if choice == 7:
    print("lucky")
else:
    print("unlucky")



# NO TOUCHING ======================================
from random import randint
num = randint(1, 1000)
# NO TOUCHING ======================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if num % 2 != 0:
    print("odd")
else:
    print("even")



# NO TOUCHING ======================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm'])
# NO TOUCHING ======================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food == 'apple' or food == 'grape':
    print ("fruit")
elif food == 'bacon' or food == 'steak':
    print("meat")
else:
    print("yuck")


    
# NO TOUCHING ======================================
from random import randint
x = randint(-100, 100)
while x == 0:  # make sure x isn't zero
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:  # make sure y isn't zero
    y = randint(-100, 100)
# NO TOUCHING ======================================

# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")



# NO TOUCHING ======================================
from random import choice, randint

actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)
# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# Note, we don't need to check if actually_sick == True
#  Instead, just check if actually_sick, since it's a boolean

if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False
    