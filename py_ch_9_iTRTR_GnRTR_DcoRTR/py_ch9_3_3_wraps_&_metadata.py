
# Courses: colt_py_bootcamps    282, 283, 284

# -----------------    Preserving Metadata    -----------------
# The "Decorated-function's" metadata (Eg: function documentation) will  be lost 
    # It will refer to "Decorator's" metadata



# Example 1: Following "Decorated-function" add() will lost it's metadata

def log_function_data(fn) :
    def wrapper(*args, **kwargs):
        """ I am a wrapper function  """
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs) 
    return wrapper


@log_function_data 
def add(x, y):
    """ Adds two numbers together """
    return x + y

# Following will print proper "Metadata"
    # the "__name__" and "__doc__" are called inside "warpper"
print(add(2, 3))


# The problem arise if we call __name__ and __doc__ outside as below
print(add.__name__)
print(add.__doc__)
# "add's" metadata won't be there, but "Decorator's" metadate wil be printed




# -----------------    functools.warps    -----------------
# To preserve the "Decorated-function's" metadata we need to use functools.warps
from cgitb import reset
from curses import wrapper
from functools import wraps
    #	wraps preserves a function's1 metadata
    #	when it is decorated
    #   NOTICE: the function "fn" is passed to @wraps() as an 'argumnet'

def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs) 
        pass
    return wrapper




# Example 2: Following "Decorated-function" add()'s metadata preserved
import functools

def log_function_data(fn):
    # metadata of DECORATED-function will be preserved now
    @functools.wraps(fn)   # the function is passed to wraps() as an argumnet
    def wrapper(*args, **kwargs):
        """ I am a wrapper function  """
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs) 
    return wrapper


@log_function_data 
def add(x, y):
    """ Adds two numbers together """
    return x + y

# Following will print proper "Metadata"
    # the "__name__" and "__doc__" are called inside "warpper"
print(add(2, 3))


# The problem is solved. Also prints add's "Metadata"
print(add.__name__)
print(add.__doc__)
help(add)




# Example 3: (SPPED-TEST) apply "Decorator" to speed test of "Generator-vs-List"
import time
import functools

def speed_test(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_tm = time.time()
        result = fn(*args, **kwargs)
        end_tm = time.time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_tm - start_tm}")
        return result
    return wrapper

@speed_test
def sum_gen():
    return sum(n for n in range(100000000))

@speed_test
def sum_list():
    return sum([n for n in range(100000000)])

print(sum_gen())
print(sum_list())

# output:
    #   Executing sum_gen
    #   Time Elapsed: 9.864956140518188
    #   4999999950000000
    #   Executing sum_list
    #   Time Elapsed: 13.556610822677612
    #   4999999950000000




# -----------------    Simpler Decorator Boilerplate    -----------------

# ignoring all the boilerplate code (the stuff that goes in every decorator function, wraps,etc.), 
    # the important logic is really just:

from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return wrapper 

# first we return 'fn' from 'wrapper'
# finally we return the "wrapper" itself from the decorator



