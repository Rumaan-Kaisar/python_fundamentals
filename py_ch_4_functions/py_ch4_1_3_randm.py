
# Courses: colt_py_bootcamps    149 

# -------------|    The random() function    |-------------
from random import random

def flip_coin():
    # generate a random number
    r = random()

    if (r < 0.5):
        print("Tail")
    else:
        print("Head")

flip_coin()


# Defineing a function again after its previous definaion 
    # will "Override" the previous definintion
    # following will override the aove function

def flip_coin():
    if (random() < 0.5):
        print("TAIL")
    else:
        print("HEAD")

flip_coin()


# python py_ch4_1_3_randm.py
