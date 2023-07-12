
# Courses: colt_py_bootcamps    285-292

# Inforce restrictions on Arguments using Decorators
    # Create a Decorator that prevent any "KWARG"
""" 
    @ensure_no_kwargs
    def func():
        . . .
        . . .
"""
    # Or prevent anyy numerical arguments

import functools

def ensur_no_kwargs(fn):
    @functools.wraps(fn)    # if "fn" not passed as argumnet in warps(), ERR occurs
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed!")
        return fn(*args, **kwargs)
    return wrapper

@ensur_no_kwargs
def greet(name):
    print(f"Hi there {name}")

greet("Tony")   # ok. No kwargs
greet(name="Tony")  # ERR, kwarg is used


# Same idea can be used for "type checking", "existance of certain argumnets"
# We can use this idea for creating dynamic decorators 




# Example 1: Create a simplest decorator boilerplate.
    # This wrapper function simply runs the function, and returns a list containing the result twice:
from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

@double_return
def sqr(num):
    return num*num

print(sqr(5))




# Example 2: Create a Decorator that limits no. of args
from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper

@ensure_fewer_than_three_args
def mul1(num1, num2):
    return num1*num2

print(mul1(5, 7))

@ensure_fewer_than_three_args
def mul2(num1, num2):
    return num1*num2

print(mul2(5, 7, 11))




# Example 3: Create a Decorator that ensures "int" inputs
from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner




# Example 4: Create a Decorator that mimics "Authorization"
from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper




# Example 5: Create a Decorator that makes a function delay to execute
from functools import wraps
from time import sleep

def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(timer, fn.__name__))
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner



# python "py_ch9_3_4_args_&_DcRTR.py"

