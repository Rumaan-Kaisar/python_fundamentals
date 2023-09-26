
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


