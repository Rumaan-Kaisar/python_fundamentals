# Courses: colt_py_bootcamps 035,036, 037, 038, 039, 040
# Topics:   ints, floats
        #   math operators
        #   commenting

"""Variables

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_variables.asp
@see: https://www.learnpython.org/en/Variables_and_Types

#       Python is completely object oriented
#       not "statically typed".
#       No need to declare variables before using them, or declare their type. 
        #       Every variable in Python is an object.
        #       A variable is created the moment you first assign a value to it.

Rules for Python variables:
- must start with a letter or the underscore.
- cannot start with a number.
- only  alpha-numeric characters and underscores (A-z, 0-9, and _ ).
- case-sensitive

"""



# --------------  ints, floats  --------------

num = 1.9
typ_of_num = type(num)
print(typ_of_num) # <class 'float'>

# type promotion int + float = float
a = 1 +1.2
print(f"sum = {a}, type = {type(a)}")



# --------------  math operators  --------------
# int + float = float; 
# int*float = float; 
# int*int = int

b = 2 + 9.0
c = 2 * 9.0
m = 2 * 9
# int/int = float
dv = 1/1
print(f"sum = {b}, division = {dv}, multp_1 = {c}, multp_2 = {m}")

# order of operations: P E M D A S - pranthesis, exponents, multiply, division, addition, subtract
od_1 = 1+2*5/3
od_2 = (1+2)*5/3
print(f"od_1 = {od_1}, od_2 = {od_2}")



# --------------  Exponent **, Modulo (remainder) %, Int-division (chopped out decimal part) //  --------------
pw = 2**4
sq_rt = 4**0.5
m_od = 9%2
dv_1 = 3/2
dv_2 = 2/3
int_dv_1 = 3//2
int_dv_2 = 2//3
print(f"Expnent = {pw}, Root = {sq_rt}, Regular_Divisiion_1 = {dv_1}, Regular_Divisiion_2 = {dv_2}")
print(f"Integer_Divisiion_1 = {int_dv_1}, Integer_Divisiion_2 = {int_dv_2}")



# --------------  comments  --------------
# singel line
''' 
multi line
multi line
multi line
'''



# Concatenation operator "+=" is used with string data-type
# We can use +=, -+ *=, /= as shorthand form for numerical datatypes
a += 2;
b -+ 3
c *= 4
d /+ 9 

#  --------------  python documentation  -------------- 
# https://docs.python.org

# python py_01_number_math.py
