
# Courses: colt_py_bootcamps    218, 219

# ----------------    Custom Modules    ----------------
    # You can import from your own code too 
    # The syntax is the same as before 
    # import from the name of the Python file
    
    # Custom modules are important for OOP and Better "Code-Organization" for Big projects 
    # Custom modules are also used to create Complex DataStructures
    

# Custom Modules Demo

# .........    file1.py	
def	fn() :	
	return "do some	stuff"

def	other_fn():	
	return "do some	other stuff"


# .........    file2.py
import file1

filel.fn()      # 'do some stuff' 
file2.other_fn()    # 'do some other stuff'




# Example 1: Use the modules apples.py and bananas.py

# Importing everythin in both modules:

import bananas
import apples

print(apples.offer())
print(bananas.dip_in_chocolate())


# Importing a single function from bananas:
from bananas import dip_in_chocolate as dip
print(dip())




# Example 2: write simple code in one file and import it into another file.

    # In "helpers.py": I started by defining lucky_number  in helpers.py:
    
    # In exercise.py: I import my "helpers"  module first.  
        # And then I call helpers.lucky_number()  and save the result to the 'num'  variable   

def lucky_number():
    return 37

#Import your helpers module here.  Do not use the 'from' or 'as' syntax, just use a plain old 'import'
import helpers

#Call the lucky_numbers function from your helpers module, and save the result to a variable called num
num = helpers.lucky_number()


