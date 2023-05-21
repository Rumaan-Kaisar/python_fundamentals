

# Courses: colt_py_bootcamps    212

# -----------------    PDB : Python Debugger    -----------------
# Silent BUG/ERR: Do not abruptly terminat the program but get different result.

# PDB: It is a module of Python 
    # if a statement terminated with an unhandled exception, 
        # you can use pdb's post-mortem facility to inspect the contents of the traceback:


# pause: To set breakpoints in our code we can use pdb by inserting this line:
import pdb; pdb.set_trace()
# Whenever this line found the execution wil pause
    # the program wont terminate or skip anything else, just pauses
    # in the terminal/cli we can interact with the values 
    # or execute one line at a time

# Common PDB Commands:
    # l (list)
    # n (next line)
    # p (print)
    # c (continue - finishes debugging)




# Example 1: Demo of using PDB
import pdb
first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

# when pdb.set_trace() appears execution pauses
    # use PDB commands to execute the rest of the code and debug




# -------------    Python multi-line    -------------
import pdb
pdb.set_trace()

# can also be written as:
import pdb; pdb.set_trace()




# -------------    PDB command name CONFLICT    -------------

# Be careful with variable names! Cannot use "c" to acces value; it will execute PDB command "c"
# to print the value use PDB command "p"
def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace() 

    return a + b + c + d
add_numbers(1,2,3,4)

'''
E:\1_Development_2.0\ML_phase_1_Python_codex\py_ch_7_exception>python test.py
> e:\1_development_2.0\ml_phase_1_python_codex\py_ch_7_exception\test.py(6)add_numbers()
-> return a + b + c + d
(Pdb) a
a = 1
b = 2
c = 3
d = 4
(Pdb) b
(Pdb) p b
2
(Pdb) p a
1
(Pdb) p d
4
(Pdb) p c
3
(Pdb) c
'''




# ===================
# NOTES  NOTES  NOTES
# ===================
# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
    # l (list)
    # n (next line)
    # p (print)
    # c (continue - finishes debugging)




# --------------    CLI    --------------

''' 

E:\1_Development_2.0\ML_phase_1_Python_codex\py_ch_7_exception>python test.py
> e:\1_development_2.0\ml_phase_1_python_codex\py_ch_7_exception\test.py(8)<module>()
-> result = first + second

# "l" will show the list

(Pdb) l
  3
  4     import pdb
  5     first = "First"
  6     second = "Second"
  7     pdb.set_trace()
  8  -> result = first + second
  9     third = "Third"
 10     result += third
 11     print(result)
 12
 13     # a = int(input("please enter a number: "))


# Accessing values

(Pdb) second
'Second'


# 9th line not executed yet

(Pdb) third
*** NameError: name 'third' is not defined


# Executing next line : 9th line

(Pdb) n
> e:\1_development_2.0\ml_phase_1_python_codex\py_ch_7_exception\test.py(9)<module>()
-> third = "Third"
(Pdb) l
  4     import pdb
  5     first = "First"
  6     second = "Second"
  7     pdb.set_trace()
  8     result = first + second
  9  -> third = "Third"
 10     result += third
 11     print(result)
 12
 13     # a = int(input("please enter a number: "))
 14     # b = int(input("please enter a number: "))

 
# 9th line not executed yet
 
(Pdb) third
*** NameError: name 'third' is not defined


(Pdb) n
> e:\1_development_2.0\ml_phase_1_python_codex\py_ch_7_exception\test.py(10)<module>()
-> result += third
(Pdb) l
  5     first = "First"
  6     second = "Second"
  7     pdb.set_trace()
  8     result = first + second
  9     third = "Third"
 10  -> result += third
 11     print(result)
 12
 13     # a = int(input("please enter a number: "))
 14     # b = int(input("please enter a number: "))
 15

# 9th lin executed
(Pdb) third
'Third'

# c (continue - finishes debugging)
(Pdb) c
FirstSecondThird

E:\1_Development_2.0\ML_phase_1_Python_codex\py_ch_7_exception>

'''




