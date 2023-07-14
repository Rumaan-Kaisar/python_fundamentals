
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

@only_ints
def mul1(num1, num2):
    return num1*num2

print(mul1(5, 7))

print(mul1(5.0, 7.0))   # Force to put int




# Example 4: Create a Decorator that mimics "Authorization"
from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper

@ensure_authorized
def mul1(num1, num2, role):
    return num1*num2

print(mul1(5, 7))   # Unauthorized

print(mul1(5, 7, role = "admin"))




# ---------------     Decorator with parameters     ---------------
# we can pass arguments to the decorator when we use it on a function

# Adding Extra layer of function to our decorator
    # we have to add an extra function layer to make a decoorator with argumnet
    # For example
        # @ensure_first_arg_is("burrito")


# following shows what is going on under the hood
# NOT WORKING CODE!

# When we write decorator with no args:
@decorator
def func( *args, **kwargs):
    pass

# We're really doing:
func = decorator(func)


# When we write a decorator with args: 
@decorator_with_args(arg)
def func( *args, **kwargs):
    pass

# We're really doing: Applying extra-layer function
func = decorator_with_args(arg)(func)




# Example 5: Enforcing First arguments.
from functools import wraps

def ensure_first_arg_is(val):   # this is the extra layer
	def inner(fn):              # this is the decorator
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val:
				return f"First arg needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner


# enforces first argument to be "burrito"
@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
print(fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10, 12)) # 12
print(add_to_ten(1, 2)) # 'Invalid! First argument must be 10'




# Example 6:  Enforcing Types whatever function we define
def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable   
            newargs = []        
            for (a, t) in zip(args, types):
                # following is type casted args
                newargs.append( t(a)) #feel free to have more elaborated convertion
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a,b):
	print(a/b)
# repeat_msg("hello", '5')
divide('1', '4')




# Example 7: Create a Decorator that makes a function delay to execute
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

@delay(5)
def mul_1(num1, num2):
    return num1*num2

print(mul_1(5, 7))   # Unauthorized


# python "py_ch9_3_4_args_&_DcRTR.py"

