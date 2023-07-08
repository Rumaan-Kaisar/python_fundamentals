
# Courses: colt_py_bootcamps    281

# --------------    Decorator with DIFFERENT SIGNATURES    --------------

# previously we had decorated functions with no arguments
# Different signatures: It means different number of argumnets here

# Decorator & Decorated: 
    # in following example "shout()" is a DECORATOR where "greet" is DECORATED

# problems with different signature (argumnets)
def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi i am {name}"

yo = greet("bo")
print(yo)


# following functio cannot be ddecorated by "shout()" because its wrapper accepts only one arg
    # Hence Type-ERR is thrown
@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

ahem = order("Book", "Tea")
print(ahem)




# -----------    *args and **kwargs wrapper    -----------
# STANDARED DECORATOR PATTERN:  More flexible
""" 
    def my_decorator(fn):
        def wrapper(*args, **kwargs):
            # do some stuff with fn(*args, **kwargs) 
            pass
        return wrapper
"""

# To resolve above problem, we need to use VARARGS in "wrapper"
    # using *args and **kwargs will help us

def shout(fn):
    def wrapper(*args, **kwrgs):
        return fn(*args, **kwrgs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi i am {name}"

yo = greet("bo")
print(yo)


# Now we can use a function with 'no args' or 'multiple args'
@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
    return "lol yo!!"


print(lol())
ahem = order("Cofee", "Book")
print(ahem)

foodie = order(main="Mocha", side="Cake")
print(foodie)

# python py_ch9_3_2_DcRTR_signtr.py

