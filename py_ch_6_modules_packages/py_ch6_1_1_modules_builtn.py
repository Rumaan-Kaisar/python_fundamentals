
# Courses: colt_py_bootcamps    214, 215

# There are different pre-build modules for different works:

    # Color document
    # Add ascii art
    # HTTP request
    # connect to a database

''' 
    ----------    OBJECTIVES    ----------
    •	Define what a module is
    •	Import code from built-in modules
    •	Import code from other files
    •	Import code from external modules using "pip"
    •	Describe common module patterns
    •	Describe the request/response cycle in "HTTP"
    •	Use the "requests" module to make requests to web apps
'''

# ----------    Why Use Modules?    ----------
    # Keep Python files small - DRY code
    # To manage you code better
    # Reuse code across multiple files by importing 
    # A module is just a Python file!




# ----------    Built-in Modules    ----------
# Built-in Modules Example
import random			
random.choice(["apple",	"banana",	"cherry", "durian"])
random.randint(1, 100)
random.shuffle(["apple",	"banana",	"cherry", "durian"])

# import module by giving it a different name
import random as oMg_rand
frt_lst = ["apple",	"banana",	"cherry", "durian"]
print(oMg_rand.choice(frt_lst))
oMg_rand.randint(1, 100)
print(oMg_rand.shuffle(frt_lst))

''' -------- CLI --------
>>> oMg_rand.shuffle(frt_lst)
>>> frt_lst
['banana', 'durian', 'cherry', 'apple']
>>> oMg_rand.shuffle(frt_lst)
>>> frt_lst
['durian', 'banana', 'apple', 'cherry'] 
'''



# ----------    Importing Parts of a Module    ----------
# Importing Parts of a Module
    # The "from" keyword lets you import parts of a module

from random import randint, choice
choice(frt_lst)
randint(1, 100)

# Importing Parts of a Module by giving different name
from random import randint as alpha, choice as beta
beta(frt_lst)
alpha(1, 100)

# Importing all Parts of a Module
from random import *

# Note:
    # From my point of view, importing parts from a module can lead to confusioin
    # Because different module can contain parts that can have same NameError
    # Resulting "Name Collision"
    # Better choice is: "module.property"




# ----------    Different Ways to Import    ----------
# All of these work!
    # •	import random
    # •	import random as omg_so_random
    # • from random import *
    # • from random import choice, shuffle
    # •	from random import choice as gimme_one, shuffle as mix_up_fruits




# Example 1: Math Module Exercise. Find square root of 15129.
import math

answer = math.sqrt(15129)




# Example 2: Find if any argument of a function Contains Keyword.

    # I start by importing keyword up top
    # Inside of contains_keyword , I look through all items in args
    # for each item, I test if it's a keyword by calling keyword.iskeyword(item) 
    # The first time we encounter a keyword, return True right away
    # Otherwise, once the loop is over return False (meaning, no keywords were found)

import keyword

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False

contains_keyword(5)     # False
contains_keyword("import")  # True
contains_keyword("def")     # True

''' 
Python provides an in-built module keyword that allows you to know about the reserved keywords of python.

The keyword module allows you the functionality to know about the reserved words or keywords 
    of Python and to check whether the value of a variable is a reserved word or not. 
'''

