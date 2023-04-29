
# Courses: colt_py_bootcamps    145, 146, 147

# -------|    OBJECTIVES    |-------
    # Describe what a function is and how they are useful
    # Explain exactly what the "return" keyword does and some of the side effects when using it
    # Add "parameters" to functions to output different data
    # Define and diagram how "scope" works in a function
    # Add "keyword arguments" to functions

    # Use the * and ** operator as parameters to a function and outside of a function
    # Leverage dictionary and tuple unpacking to create more flexible functions
    

# =============    SUMMERY    =============
    # Functions are procedures for executing code. 
        # They accept 'inputs' and return 'outputs' when the 'return' keyword is used

    # To create 'inputs', we make parameters which can have 'default values', 
        # we call those 'default parameters' 

    # variables defined inside of functions are 'scoped' to that function - watch out for that!

    # When invoking a function we can pass in 'keyword arguments' in any order!

    # Be careful to not 'return' too early in your conditional logic and refactor when you can to remove unnecessary conditional logic. 
        # Make sure you don't 'return' in a loop too early as well!



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



# Example 5: Define a function that finds last element of a list
    # First check to see if the list exists (if it has data in it).  
    # If it does, return the '-1'st item (last item).  Otherwise, return None.

def last_element(l):
    if l:
        return l[-1]
    return None




# Example 6: Define a function that compares two numbers
def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"




# Example 7: Define a function that counts a given letter from a given string.
    # In my solution, I use the built-in count()  to count the number of times letter  appears in string .  
    # I also downcase both string  and letter  to make it "case-insensitive" (you could also upcase both instead)

def single_letter_count(string, letter):
    return string.lower().count(letter.lower())    



# Example 8: Define a function that counts multiple-letters appeared in a given string.
    # I used a "DICTIONARY COMPREHENSION". 
    # For each letter in the input string, I make the "key" the letter itself ("a" for example), 
        # and the corresponding "value" is the result of running count() of that letter in the string.

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

