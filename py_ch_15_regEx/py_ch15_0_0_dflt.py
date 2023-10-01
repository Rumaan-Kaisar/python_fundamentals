
################# 348: FULL
# copy:  
#        
#        
################# (26-sep-23 for 27-sep-23)

# Courses: colt_py_bootcamps    348, 350


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





################# 352: full
# copy:  
#        
#        
################# (1-oct-23 for 3-oct-23)

# Courses: colt_py_bootcamps    352


# ----------    compilation flag    ----------
    # we can set them to compile a RegEx in a specific way

""" 
    ASCII, A    : Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
    DOTALL, S   : Make '.' match any character, including newlines.
    IGNORECASE, I   : Do case-insensitive matches.
    LOCALE, L   : Do a locale-aware match.
    MULTILINE, M    : Multi-line matching, affecting ^ and $.
    VERBOSE, x (for 'extended') : Enable verbose REs, which can be organized more cleanly and understandably 
"""

# here we'll discuss:
                        # IGNORECASE    : to ignore UPPER/LOWER cases
                        # VERBOSE       : allows us to define regEx in multiple lines with comments (info)


import re


# -----    VERBOSE:
# consider following pattern, notice no UPPERCASE are allowed
pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')
# its very hard to undersatnd a RegEx, if it's getting very big
# it could be less difficult if 'verbose-flags' are used
    # put into 'multple lines' and adding COMMENTS

# VERBOSE lets you organize and indent the RE more clearly. 
#     This flag also lets you put comments within a RE that will be ignbred by the engine

#     When this flag has been specified, 'whitespace within the RE string' is ignored,
#         Use an UNESCAPED BACKSLASH to use whitespace




# Example 1: For example, here’s a RegEx that uses re.verbose; see how much easier it is to read?
charref = re.compile(r"""
    &[#]	                # Start of a numeric entity reference
    (
        0[0-7]+	            #	Octal form
        | [0-9]+	        #	Decimal form
        | x[0-9a-fA-F]+     #	Hexadecimal form
    )
    ;	                    #	Trailing semicolon
""", re.VERBOSE)
# Notice " " " is used

# Above RegEx without the verbose setting, the RE would look like this:
charref = re.compile(   "&#(0[0-7]+"
                        "|[0-9]+"
                        "|x[0-9a-fA-F]+);")




# Example 2: we convert following RegEx into verbose setting
                # pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

import re
pattern_1 = re.compile(r"""
                            ^([a-z0-9_\.-]+)        # first part of email	
                            @                       # single @ sign
                            ([0-9a-z\.-]+)          # email provider
                            \.                      # single period
                            ([a-z\.]{2,6})$         # com, org, net, etc.
""", re.VERBOSE)
# notice no UPPERCASE are allowed
match = pattern_1.search("thomas123@yahoo.com")
print(match.group())
print(match.groups())


# instead of "VERBOSE" name we can use "X" (extand)
import re
pattern_1 = re.compile(r"""
	^([a-z0-9_\.-]+)	#first part of email	
	@					#single @ sign
	([0-9a-z\.-]+)		#email provider
	\.					#single period
	([a-z\.]{2,6})$		#com, org, net, etc.
""", re.X)
# any uppercase letter will give ERR
match = pattern_1.search("thomaS123@yahoo.com") # ERR
print(match.group())    # ERR




# Ignore case:
#------------    multiple Flags    ------------
    # to use both "VERBOSE" and "Ignore case" we use 're.X | re.I'
    # we cannot use comma 're.X , re.I' because it doesn't support 2-flags as 2-argumnets
    # multiple Flags can be used by Bitwise Or-ing them e.g. 're.X | re.I' uses both 'X' and 'I' flags

# Example 3: we convert following RegEx into verbose & ignore-case setting
# Without Verbose Flag ...
import re
pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

# above pattern usnig VERBOSE & IGNORECASE
pattern = re.compile(r"""
	^([a-z0-9_\.-]+)	#first part of email	
	@					#single @ sign
	([0-9a-z\.-]+)		#email provider
	\.					#single period
	([a-z\.]{2,6})$		#com, org, net, etc.
""", re.VERBOSE | re.IGNORECASE)


# using short forms - X:VERBOSE, I:IGNORECASE
pattern = re.compile(r"""
	^([a-z0-9_\.-]+)	#first part of email	
	@					#single @ sign
	([0-9a-z\.-]+)		#email provider
	\.					#single period
	([a-z\.]{2,6})$		#com, org, net, etc.
""", re.X | re.I)

# Now ignore-case and verbose bith are applied
    # using uppercase won't cause any ERR
match = pattern.search("ThomaS123@Yahoo.com")
print(match.group())
print(match.groups())




