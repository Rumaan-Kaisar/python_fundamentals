
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




# Example 1: 're' module demo
import re
# patrn = re.compile('\\d{3}')     # '\\' is used if 'r' is not used
patrn = re.compile(r'\d{3} \d{3}-\d{4}')     # '\\' is used if 'r' is not used, for escape characters
print(patrn)
print(type(patrn))  # <class 're.Pattern'>

>>> help(patrn)

""" 
Help on Pattern in module re object:
class Pattern(builtins.object)
 |  Compiled regular expression object.
 |
 |  Methods defined here:
 |
 |  __copy__(self, /)
 |
 |  __deepcopy__(self, memo, /)
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 """
# '-- More --' means there is more information to display on this by pressing the Enter or space key.


# ---------------    search()    ---------------
    # Scan through string looking for a match, and return a corresponding match object instance.
    #     Return None if no position in the string matches.

    # we'll focus on the 'search' method

rslt = patrn.search("cdfgdhjfg 12335t5v356")
print(rslt)     # None

rslt = patrn.search("call me at 123 456-6789")
print(rslt)     # <re.Match object; span=(11, 23), match='123 456-6789'>

# To view the match we use group() method
rslt.group()    # '123 456-6789', returned as 'str'

# It doesn't support finding 'more than one match'
# if we have multiple matches group() only returns the first match
rslt_2 = patrn.search("call me at 310 445-9876 or 310 234-9999")
rslt_2.group()  # '310 445-9876'



# ---------------    findall()    ---------------
    # it returns the list of multiple matches
rslt_3 = patrn.findall("call me at 310 445-9876 or 310 234-9999")   # returns a list obgect
type(rslt_3)    # <class 'list'>
print(rslt_3)   # returns a list directly ['310 445-9876', '310 234-9999']



# ---------    COMPILE Once or Each time    ---------
# we can pass a pattern as argument 
    # if the pattern varies time to time
    # in this case pattern compile each time
    # prreviously we compiled the pattern ONCE

compile_and_search = re.search(r'\d{3} \d{3}-\d{4}', "call me at 310 445-9876 or 310 234-9999")
print(compile_and_search.group())

compile_and_findAll = re.findall(r'\d{3} \d{3}-\d{4}', "call me at 310 445-9876 or 310 234-9999")
print(compile_and_findAll)

# It's a good practice to COMPILE the pattern once and then use it to find matches


