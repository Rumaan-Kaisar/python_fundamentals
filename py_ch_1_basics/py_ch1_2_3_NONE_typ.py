# Courses: colt_py_bootcamps 47

# ------------ NONE type --------------
""" The None keyword is used to define a null value, or no value at all.
None is not the same as 0, False, or an empty string. 
None is a data type of its own (NoneType) and only None can be None. """

# Use : Initialize a variable, with no value at all.

name = "Daisy"
age = 38
child = None    # initialized with no value, it mostly used in object creation
#  if "child = None" not set, print(child) returns an ERR

x = None

if x:
  print("Do you think None is True?")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")