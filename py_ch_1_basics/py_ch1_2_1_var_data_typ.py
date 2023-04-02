# Courses: colt_py_bootcamps 41, 42, 44, 45
# Topics:   strings
        #   assign & use varibles
        #   variablee  namiing & conventions
        #   different data-types
        #   dynamically typed language
        #   converting data types
        #   ins & outs of strings
        #   cli user input

# variable_name = value
from subprocess import BELOW_NORMAL_PRIORITY_CLASS


x =  100
khaleesi_mother_of_dragon = 1
print(khaleesi_mother_of_dragon + x)


""" Variables can be assigned to other variables
Also ca be re-assigned at any times """

tylor = x;
x = khaleesi_mother_of_dragon * 2


# Multiple variable asignment 
all, at, once = 5, 10, 15
print(f"At = {at}, once = {once}, all = {all}")


# Naming restrictions
""" start letter or underscore
    _cats
no other symbol than letter, numbers, underscore
    cats@BELOW #wrong, @ used for operators
Case-sensitive """


# Naming onvention
""" 
    sanke_case
    variables_lower_case
    GLOBAL_CONST
    ClassCamelCase
    _no_touchy_ # dunders are supposed to be private or left alone 
"""




# ---------   Data Types  ---------
""" 
    bool    True or False
    int     Integers
    str     Strings of unicode chars
    list    an ordered sequence
    dict    collection of key: value pairs

    Text Type:	    str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	    set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	    NoneType 
"""

# Getting the Data Type
x = 5
print(type(x))

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

x = "Hello World"	                            # str	
x = 20	                                        # int	
x = 20.5	                                    # float	
x = 1j	                                        # complex	
x = ["apple", "banana", "cherry"]	            # list	
x = ("apple", "banana", "cherry")	            # tuple	
x = range(6)	                                # range	
x = {"name" : "John", "age" : 36}	            # dict	
x = {"apple", "banana", "cherry"}	            # set	
x = frozenset({"apple", "banana", "cherry"})	# frozenset	
x = True	                                    # bool	
x = b"Hello"	                                # bytes	
x = bytearray(5)	                            # bytearray	
x = memoryview(bytes(5))	                    # memoryview	
x = None	                                    # NoneType


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")	                        # str	
x = int(20)	                                    # int	
x = float(20.5)	                                # float	
x = complex(1j)	                                # complex	
x = list(("apple", "banana", "cherry"))	        # list	
x = tuple(("apple", "banana", "cherry"))	    # tuple	
x = range(6)	                                # range	
x = dict(name="John", age=36)	                # dict	
x = set(("apple", "banana", "cherry"))	        # set	
x = frozenset(("apple", "banana", "cherry"))	# frozenset	
x = bool(5)	                                    # bool	
x = bytes(5)	                                # bytes	
x = bytearray(5)	                            # bytearray	
x = memoryview(bytes(5))	                    # memoryview

test_view = frozenset({"a", "b", "12"})
test_view_2 = frozenset({"c", "b", "a"})
print(test_view)
print(type(test_view))

# union
print(test_view.union(test_view_2))  # Output: frozenset({'c', '12', 'b', 'a'})

# intersection
print(test_view.intersection(test_view_2))  # Output: frozenset({'b', 'a'})

# difference
print(test_view.difference(test_view_2))  # Output: frozenset({'12'})

# symmetric_difference
print(test_view.symmetric_difference(test_view_2))  # Output: frozenset({'12', 'c'})



some_string = "olla i am a string"
print(some_string)



# Define a variable named city and set it equal to any string
city = "Los Angeles"

# Define a variable named price and set it equal to any float
price = 5.4

# Define a variable named high_score and set it equal to any int
high_score = 100002

# Define a variable named is_having_fun and set it to a Boolean value
is_having_fun = True




