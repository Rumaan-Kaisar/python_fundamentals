
# Courses: colt_py_bootcamps    345

# ---------------    RE: RegEx in python    ---------------
# usage of RegEx in Python:
    # match a string
    # define a function that returns true if something matches a pattern
    # define a function that 'extracts' all 'matches' from a given string and returns them in a list

# you should learn the useful-functions from the 're' module documnetation
    # compile
    # search
    # match
    # split
    # findall
    # sub

# What we'll do:
    # defining a regular expression as a string 
    # compiling it into a regular expression object and 
    # using that to find matches in another string.


# -------------    using RegEx in python    -------------
# import regex module 
import re

# define our phone number regex, (make an object using compile() )
pattern = re.compile(r'\d{3} \d{3}-\d{4}')  
# note: 
    # re.compile() creates a RegEx object that contain useful RegEx methods
    # 'r' stands for raw-string

# search a string with our regex (using search() )
result = pattern.search('Call me at 415 555-4242!')
    # it gives us a "match-object"


# 3:37


