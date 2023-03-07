# Courses: colt_py_bootcamps 58

# -----------   convert data types   -----------
# In string interpolation/format, all data types are implicitly converted to string
# we can explicitly convert any data type
decimal = 3.14159
integer = int(decimal)  # Converts float to int
print(f"decimal {decimal} has type {type(decimal)}\n")
print(f"integer {integer} has type {type(integer)}\n")

# list to string
list_1 = [1, 2, 3]
print(f"list_1 {list_1} has type {type(list_1)}\n")

str_1 = str(list_1)
print(f"str_1 {str_1} has type {type(str_1)}\n")

# divition of two int auto-converted to float
a = 1
b = 2
print(f"2/1 = {b/a} has type {type(b/a)}\n")

# Converting int or float string 
str_a = str(a)
print(f"str_a {str_a} has type {type(str_a)}\n")
pia = 3.14159
str_pia = str(pia)
print(f"str_pia {str_pia} has type {type(str_pia)}\n")


# Note: do not give any identifier a name as 'str' or 'int' it will overwrite the Python built-in data-type keyword