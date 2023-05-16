
# Courses: colt_py_bootcamps    207, 208
""" 
    ----------    Debugging    ----------

    Objectives:
        Explain common errors and how they occur in python
        Use "pdb-python debugger" to set "breakpoint" and step through code
        Use "Try" and "Except" blocks to handle Errors 
"""

# ----------    Some common errors    ----------

        # SymtaxError
        # Name Error
        # Type Error
        # Index ERR
        # Value error
        # Key Error
        # Attribute Error

# There are many other errors, if you encounter one, just copy its name and GOOGLE
# more on Python Docs

# SymtaxError: 
    # incorrect syntax
    # typos

def first: # no () causes ERR

None = 1    # Syntax ERR

return    # Syntax ERR


# Name Error: When a variable is not defined or hasn't been assigned
print(test_1)   # name ERR


# Type Error:
    # operation/function applied to wrong type
    # Python cand interpret an operation on two data types

len(5)  # Type Err: len() is not  applicable to Number

"always" + []   # type ERR: cannot concatenate "str" and "list" objects



# Index ERR: Accessing invalid indexed-item from a list
list_1 = [1]
print(list[2])  # Index ERR, there is no 3rd idem in the list
nam = "Bahama"
print(nam[7])   # index Err


# Value error: Operation/function receives right type but inappropriate value
int("10")   # converts str "10" to Number 10
int("Ten")   # Value ERR: invalid lietral


# Key Error: Ocuurs in dictionary if the KEY is not present
d = {}
d["foo"]    # Key ERR : no "foo" is there


# Attribute Error: If a variable does not have that attribute (or function)
"hello".foo     # AttributeError: 'str' object has no attribute 'foo'
[1,2,3].meh()   # AttributeError: 'list' object has no attribute 'meh'
"".join(['a', 'c'])     # works: 'ac'
"".joint(['a', 'c'])     # ERR: AttributeError: 'str' object has no attribute 'joint'. Did you mean: 'join'?





