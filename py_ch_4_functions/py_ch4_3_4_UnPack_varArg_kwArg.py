
# Courses: colt_py_bootcamps    180, 181, 182, 183

# ==========     List Unpacking     ==========
# -------------    Problem passing List/Tuple to *args    -------------
    # Using * as an Argument (during function call): Argument Unpacking
    # We can use * as an argument to a function-call to "unpack" values like "List" or "Tuple"

def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

# sum_all_values(1,30,2,5,6)
    # args: (1, 30, 2, 5, 6)

# following returns ERROR
nums = [1,2,3,4,5,6]
sum_all_values(nums)    # ERROR
    # args: ([1, 2, 3, 4, 5, 6],), list is stored as an element of the *args tuple

# -----------    unpacking list    -----------
# to unpack the list and pass its elemens as individual arguments to *args, we need to use '*' in the function call
sum_all_values(*nums)   # works
    # args: (1, 30, 2, 5, 6)


# -----------    unpacking Tuple    -----------
# following also returns ERROR
nums2 = (1,2,3,4)
sum_all_values(nums2)    # ERROR
#  args: ((1, 2, 3, 4),) tuple is stored as an element of the *args tuple
sum_all_values(*nums2)   # works




# Example 1: Simple Unpacking Exercise Solution
# Here's what you were given:

def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

# First, call count_sevens  with the numbers: 1,4, and 7  (review)
result1 = count_sevens(1,4,7)

# Next, call count_sevens  with all the values from the "nums"  list, unpacked:

result2 = count_sevens(*nums)
# Adding that little '*'  makes a huge difference! Instead of passing in a single item (the list), we're now passing in 121 separate arguments.




# ==========     Dictionary Unpacking     ==========
# -------------    Problem passing Dictionaries to **kwargs    -------------
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Charlie", "second": "Snoopy"}

display_names(names) # ERR..
display_names(**names)  # yup!


# Unpacking can also work independent of **kwarg in function-definition
def add_and_multiply_numbers(a,b,c):
    print(a + b * c)

data_1 = dict(a=1,b=2,c=3)
add_and_multiply_numbers(data_1)    # ERR
add_and_multiply_numbers(**data_1)    # unpacked!!




# Example 2: Dictionary unpacking along with **kwarg in function-definition
def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data_2 = dict(a=1,b=2,c=3)
add_and_multiply_numbers(**data_2)  # kwarg left unused

data = dict(a=1,b=2,c=3,d=55,name="Tony")
add_and_multiply_numbers(**data) 
# 7
# OTHER STUFF....
# {'d': 55, 'name': 'Tony'}




# Example 3: Following perfoms arithmetic operations using **kwarg
# Calculate Walkthrough
# This solution uses dict.get() a lot. 
    # dict.get('first')  will return the value of 'first' if it exists, otherwise it returns None.  
        # However, you can specify a second argument which will replace None as the default value. I use that in this solution a bunch of times.

    # I defined a dictionary called "operation_lookup"  that maps a string like "add" to an 
        # actual mathematical operation involving the values of 'first' and 'second'

    # I create a boolean variable called "is_float", which is "True" if kwargs contains 'make_float', otherwise it's "false"

    # Then I lookup the correct value from the 'operation_lookup' dict using the operation that was specified in kwargs
        # Basically, turning something like "subtract" into: kwargs.get('first', 0) - kwargs.get('second', 0) 
        # Which in turns simplifies to a number
        # I store the result in a variable called "operation_value" 

    # I return a string containing either the specified message or the default 'The result is' string.  
        # Whether operation_value  is interpolated as a float or int is determined by the is_float  variable.
        # Note: this solution will divide by zero if a 2nd argument isn't provided for divide.  You may want to change the default value to 1. 

def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }

    is_float = kwargs.get('make_float', False)

    operation_value = operation_lookup[kwargs.get('operation', '')]

    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

calculate(operation = "multiply", make_float = True, first = 56, second = 56)
# 'The result is 3136.0'



''' 
Syntax
        dictionary.get(keyname, value)

    keyname =	Required. The keyname of the item you want to return the value from
    value =	Optional. A value to return if the specified key does not exist. Default value None.
'''



# Run in cmd: To run in cli, remove the carrige return (line breaks)
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

