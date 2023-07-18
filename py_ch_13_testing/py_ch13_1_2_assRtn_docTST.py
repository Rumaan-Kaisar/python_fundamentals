
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

# >>> called "MINGLING-SYNTAX" 




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




# Example 4: How to execute a DOCTEST.
def add(a, b):
	"""
	>>> add(2, 2)
	4
	>>> add(2, 3)
	5
	>>> add(100,200)
	300
	"""
	# return a + b
	return a*b # Returns DOCTEST ERR


# -----------    Execution of DOCTEST in CLI    -----------
# python -m doctest -v file_name.py
# python -m doctest -v test.py


# Running with "a*b" instead of "a+b"
H:\shared_docs\codes_py\py_ch_13_testing>python -m doctest -v test.py
Trying:
    add(2, 2)
Expecting:
    4
ok
Trying:
    add(2, 3)
Expecting:
    5
**********************************************************************
File "H:\shared_docs\codes_py\py_ch_13_testing\test.py", line 33, in test.add
Failed example:
    add(2, 3)
Expected:
    5
Got:
    6
Trying:
    add(100,200)
Expecting:
    300
**********************************************************************
File "H:\shared_docs\codes_py\py_ch_13_testing\test.py", line 35, in test.add
Failed example:
    add(100,200)
Expected:
    300
Got:
    20000
1 items had no tests:
    test
**********************************************************************
1 items had failures:
   2 of   3 in test.add
3 tests in 2 items.
1 passed and 2 failed.
***Test Failed*** 2 failures.




# Example 5: Following DOCTEST passes all cases
def muLt(n, m):
	""" 
	>>> muLt(5, 6)
	30
	>>> muLt(0.5, 0.5)
	0.25
	"""
	return n*m

# CLI>>> python -m doctest -v test.py

Trying:
    muLt(5, 6)
Expecting:
    30
ok
Trying:
    muLt(0.5, 0.5)
Expecting:
    0.25
ok
1 items had no tests:
    test
1 items passed all tests:
   2 tests in test.muLt
2 tests in 2 items.
2 passed and 0 failed.
Test passed.





# Example 6: Folowing code written wwith TDD
def double(values):
	""" double the values in a list

	Note: we have to mimic exat same REPL output, eg: [2,4,6,8] instead of [2, 4, 6, 8]
			(no-space) will cause Fail the case

	>>> double([1,2,3,4])
	[2, 4, 6, 8]

	>>> double([])
	[]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']

	Note: we have to copy exat same ERR msg
	>>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
	"""
	# TDD
	# return []
	return [2 * element for element in values]




# ----------------     NOTE : Issues with doctests     ----------------

	# Syntax is a little strange : It's kind of "Mine-field", we have to mimic exact REPL

	# Clutters up our function code : Usually small functions get longer

	# Lacks many features of larger testing: We have to replicate similar test for different functions
	# 	using unittest will help on this, we cab run same kind of test for different functions

	# Tests can be brittle


# 1. Doctests can only compare to SINGLE QUOTED strings. Following cause test failure
def say_hi():
	"""
	>>> say_hi()
	"hi"
	"""
	return "hi"



# 2. Watch out for whitespace!
# (There's a trailing space on line "True ")
def true_that():
	"""
	>>> true_that()
	True 
	"""
	return True



# 3. Order of keys in dicts matters in doctests
def make_dict(keys):
	"""
	>>> make_dict(['a','b'])
	{'b': True, 'a': True}
	"""
	return {key: True for key in keys}

# Above 3 tests wil fail Even-if they look ok!!! We have to mimic REPL




