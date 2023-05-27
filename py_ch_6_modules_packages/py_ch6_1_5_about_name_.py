
# Courses: colt_py_bootcamps    223

# -----------------    __name__    -----------------
# Python has a built-in variable called __name__ that records the name of the currently running module or script. 
# The __name__ variable merely holds the name of the module or script unless the current module is executing, in which case the value __main__ is set to it.


''' 
Since there is no main() function in Python, when the command to run a python program is given to the interpreter, 
    the code that is at level 0 indentation is to be executed. 

    However, before doing that, it will define a few special variables. 
    __name__ is one such special variable. 

        If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. 
        If this file is being imported from another module, __name__ will be set to the "module’s name".

__name__ is a built-in variable which evaluates to the name of the "current module". 
    Thus it can be used to check whether the current script is being run on its own or being imported somewhere else by  
    combining it with if statement, as shown below.
'''
    

# Consider two separate files File1 and File2.

# File1.py 
  
print ("File1 __name__ = %s" %__name__) 
  
if __name__ == "__main__": 
    print ("File1 is being run directly")
else: 
    print ("File1 is being imported")
 

# File2.py 
  
import File1 
  
print ("File2 __name__ = %s" %__name__) 
  
if __name__ == "__main__": 
    print ("File2 is being run directly")
else: 
    print ("File2 is being imported")


# Now the interpreter is given the command to run File1.py.
python File1.py

# Output :
# File1 __name__ = __main__
# File1 is being run directly


# And then File2.py is run.
python File2.py
# Output :
# File1 __name__ = File1
# File1 is being imported
# File2 __name__ = __main__
# File2 is being run directly

    # when File1.py is run directly, the interpreter sets the __name__ variable as __main__  
    # when it is run through File2.py by importing, the __name__ variable is set as the name of the python script, i.e. File1. 


# ----------    using __name__ and __main__ with imported files    ----------

# When run, every Python file has a__name____variable
# Default: If the file is the main file being run, its value is "_main
# Otherwise, its value is the (imported) file name

# When you use import, Python...
# 1.	Tries to find the module (if it fails, it throws an error),
# 2.	Runs the code inside of the module being imported,

# Ignoring Code on Import
if __name___ == "__main__":
    #	this code will only run
    #	if the file is the main file!


