
# Courses: colt_py_bootcamps    145, 146, 147

# -------|    OBJECTIVES    |-------
    # Describe what a function is and how they are useful
    # Explain exactly what the "return" keyword does and some of the side effects when using it
    # Add "parameters" to functions to output different data
    # Define and diagram how "scope" works in a function
    # Add "keyword arguments" to functions


# What is a Function?
    # A process for executing a task
    # It can accept input and return an output
    # Useful for executing similar procedures over and over


# Why Use Functions?
    # Stay "DRY" - Don't Repeat Yourself!
    # Clean up and prevent code duplication 
    # "Abstract away" code for other users 
        # Imagine if you had to rewrite the "print()" function for every program you wrote



# -------|    Function Structure    |-------
def name_of_function(params):
    # Code Block to execute

# Execute: To execute a function always call the function with "()"
name_of_function(args)




# Example 1: Define and execute a function
def say_my_name():
    print(f"You're Heisenberg!!")

say_my_name()   # You're Heisenberg!!




# Example 2: Another simple function
def sing_happy_birthday():
    print("Happy Birthday To You") 
    print("Happy Birthday To You") 
    print("Happy Birthday Dear 'Blah! Blah Blah!'") 
    print("Happy Birthday To You")

sing_happy_birthday()




# Example 3: Define make_noise with parameters
def make_noise(nm_prm):
    print(f"THE {nm_prm} GOES WILD")

# Execute make_noise:
make_noise("GAGNAM")




# Example 4: Define a function "product" that returns the product of two numbers:
def product(a,b):
    return a*b




