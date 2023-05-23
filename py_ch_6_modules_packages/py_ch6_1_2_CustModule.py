
# Courses: colt_py_bootcamps    218

# ----------------    Custom Modules    ----------------
    # You can import from your own code too 
    # The syntax is the same as before 
    # import from the name of the Python file
    
    
    
# Importing everythin in both modules:

# import bananas
# import apples

# print(apples.offer())

# print(bananas.dip_in_chocolate())


# Importing a single function from bananas:
from bananas import dip_in_chocolate as dip
print(dip())




Custom Module Exercise
This exercise tested your ability to write simple code in one file and import it into another file.

In helpers.py:
I started by defining lucky_number  in helpers.py :

def lucky_number():
    return 37
In exercise.py:
I import my helpers  module first.  And then I call helpers.lucky_number()  and save the result to the num  variable

#Import your helpers module here.  Do not use the 'from' or 'as' syntax, just use a plain old 'import'
import helpers


#Call the lucky_numbers function from your helpers module, and save the result to a variable called num
num = helpers.lucky_number()
