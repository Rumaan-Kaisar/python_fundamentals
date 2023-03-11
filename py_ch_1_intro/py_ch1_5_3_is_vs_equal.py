# Courses: colt_py_bootcamps 71

""" 
    In Python "==" and "is" are very similar "comparators"
    a = 1
    a == 1  # true
    a is 1  # true

    == compares the 'values'

    'is' actually cheks if the objects share/located in the same memory
        It cheks if they are actually the same object, with the 'same memory location'.
        It used to compare the objects
    
    'is' is only truthy if the variables reference the same item in 'memory'

"""

a = [1, 2, 3]
b = [1, 2, 3]

a == b  # True, because values are the same
print(a == b)
a is b  # False, because they are not the same object, don't have the 'same memory location'
print(a is b)

c = b   # pointing same memory location where "b" is
c is b  # true

# But note that, for literals like int or float we get different result
# because these are not objects
x = 14
y = 14
print(x == y)   # True
print(x is y)   # True, because x , y are not objects, they point to a literal value
