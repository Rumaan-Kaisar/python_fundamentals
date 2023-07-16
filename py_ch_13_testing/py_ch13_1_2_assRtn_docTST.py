
# Courses: colt_py_bootcamps    295, 296

# -----------------    ASSERTIONS    -----------------
# 'assert' keyword:
	# Wc can make simple assertions with the "assert" keyword
	# 'assert' accepts an 'expression'
	# Returns None if the expression is 'truthy'
	# Raises an 'assertionerror' if the expression is 'falsy'
	# Accepts an 'optional error message' as a second argument

	# syntax:
		# assert expression, error_msg




# Example 1: Following assertion makes sure that both numbers are positives

def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
	# assert	expression	,	error_msg
    return x + y

print(add_positive_numbers(1, 1)) # 2
add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive!

# We can think assertion as following 'if-sataement'
	# if not some_expression: raise AssertionError()
	# slight difference: in optimized mode we can override it

assert 4==4	# true
assert 2==4, "4 should not Equal to 2"	# AssertionError




# Example 2: Force to input listed junk-food
def eat_junk(food):
	assert food in [
		"pizza", 
		"ice cream", 
		"candy", 
		"fried butter"
	], "food must be a junk food!"
	return f"NOM NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))




# ----------------    -O flag    ----------------
# assertion warnings:
# Running python in optimized mode:
	# If a Python file is run with the -O flag, assertions will not be evaluated!
		# i.e assertions will be ignored

# assuming the above code is saved in a .py file called "junkFood.py"
	# following is the way to run it in optimized mood (with -O flag), using uppercase -O
python -O junkFood.py




# That's why assertion is NOT TOTALLY SAFE, consider following demo 
	# We sould not do iportant stuff with assertions, 

# Don’t write code like this!
def do_something_bad(user):
	assert user.is_admin, "Only admins can do bad things!" 
	destroy_a_bunch_of_stuff()
	return "Mua ha ha ha!"





# -----------------    DOCTESTS    -----------------
# Remember the "DOCSTRING", which is used to provide documnetation to a function
# We can use this "DOCSTRING" for testing
	# Python can running and parsing those test code for us
	# We have to write our code in a very particualar way

# DOCTESTs:
	# We can write tests for functions inside of the docstring 
	# REPL-kind: Write code that looks like it's inside of a REPL
	# Covers both: It is a Human-Readable Documentation and also it runs as TEST




# Example 3: Following is a demo of DOCTEST pattern
def add(x, y):
	"""add together x and y

	>>> add (1, 2)
	3

	>>> add ( 8 , "hi")
	Traceback (most recent call last):
	...
	TypeError: unsupported operand type(s) for + :	'int' and 'str'
	"""
# NOTE: It shoud match the "INPUT - >>>" and "OUTPUT" - REPL

=========     1:27



# ------------    Doctest demo    ------------
def add(a, b):
	"""
	>>> add(2, 3)
	5
	>>> add(100,200)
	300
	"""
	return a + b

def double(values):
	""" double the values in a list

	>>> double([1,2,3,4])
	[2, 4, 6, 8]

	>>> double([])
	[]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']

	>>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
	"""
	return [2 * element for element in values]

# Doctests can only compare to single quoted strings
def say_hi():
	"""
	>>> say_hi()
	"hi"
	"""
	return "hi"

# Watch out for whitespace!
# (There's a trailing space on line 42)
def true_that():
	"""
	>>> true_that()
	True 
	"""
	return True

# Order of keys in dicts matters in doctests
def make_dict(keys):
	"""
	>>> make_dict(['a','b'])
	{'b': True, 'a': True}
	"""
	return {key: True for key in keys}






