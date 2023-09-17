
# Courses: colt_py_bootcamps    339. 340

# it's not a python specific topic


# --------------    REGULAR EXPRESSIONS    --------------

    # A way of describing patterns within search strings
        # It's a setup of some special characters that match some patterns.

# e.g: Validating Emails:
    # to check a string is an email or not, we need very complex logic
        # instead we can use "regex"

    # If we want to implement without "RegEx", we have to implement following logic

            # Starts with 1 or more letter, number, +, -, _, .
                # then
            # A single @ sign 
                # then
            # 1 or more letter, number, or - 
                # then
            # A single dot 
                # then
            # ends with 1 or more letter, number, -, or .

        
        # we can do the same thing using following RegEx

            #   (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

                #   we can devide it nto following parts

                        #   ^[a-zA-Z0-9_.+-]    : ^ means 'start with' and "can repeat"
                        #   @
                        #   [a-zA-Z0-9-]
                        #   \.                  : it's just a .
                        #   [a-zA-Z0-9-.]
                        #   $    : $ means 'ends with

                # note that, above RegEx is not python specific, it's a general RegEx
                    # we need to convert it into python specific code
                    # we'll use python 'regex' module for that



# -----    POTENTIAL USE CASES    -----
    # Credit Card number validating
    # Phone number validating
    # Advanced find/replace in text
    # Formatting text/output
    # Syntax highlighting

def hello_world(thingy):
    # I do nothing 
    print("Hello World!")




# --------------    RegEx outside of python    --------------
# There is a browser tool to test any RegEx as "Live"
    # pythex: It's a pyython specific RegEx tester

# There are a ton of REGEX SYMBOLS.
    # we're just going to cover some important ones
    # dont need to know all symbols, just cover most usefull ones and use StackOverlow
    # use RegEx cheatsheet/online e.g. : Rex Egg



# pythex: It's a pyython specific RegEx tester
        # Copy and paste any text-strings
        # type regular characters: a, b, c
        # use \ as escape charcters
        # '.' means select-all, use '\.' to select '.'


# Group 1 : RegEx Syntax
""" 
        \d  digit 0-9: 
                        \d selects 9, 99, 123; each digits seperately
                        \d\d selects all 2-digit nubers: 12, 99
                        \d \d: selects numbers with space between them; 3 3, 8 4
        
        \w  letter, digit, or underscore (word-characters)
                        \w \w: selects letters & space but no newline or tabs
                        \w\s\w: selects all lettes with 'space in between'

        \s  whitespace character: Tabs, Newlines

        \D  not a digit

        \W  not a word character:
                        \W: selcts all non-word characters: spaces , . 

        \S  not a whitespace character

        .   any character except line break

        Notice: uppercase is used for 'negation'
"""

# Select all 5-letter words:
    # " \w\w\w\w\w": didnt catch all, instead use
    # "\s\w\w\w\w\w\s"


