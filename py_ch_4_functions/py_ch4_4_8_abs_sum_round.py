
# Courses: colt_py_bootcamps    198, 199, 200, 201

# ----------------    abs()    ----------------
# returns absolute of a number, argument may be int or float
abs(5)  # 5
abs(-5) # 5

# using string will return ERR
abs("20")   # ERR
# Need to cast properly
# float("-39")    # -39.0
abs(float("-39"))   # 39.0

# math.fabs() : do the same thing but for the floats
import math
math.fabs(-39)  # 39.0
math.fabs("-39")    # ERR




# ----------------    sum()    ----------------
# takes an iterable and start (opt.)
# returns sum of the start and the items of the iterable from left to right
# start is 0 by default
# can work with list, tuple or set

# it doesn't work with string, use ''.join(sequence) instead

# It first adds the start and then the items of the list
sum([1,2,3,4,5], -20)
sum([1,2,3,4,5], 5)
sum([1,2,3,4,5], 0)

sum((2, 3, 7))  # tuple
sum({2, 3, 7})  # set

# To add floating values more precisely, use math.fsum()
import math
math.fsum({2.9, 3.965, 7.96})




# ----------------    round()    ----------------
# round the number "ndogits" pricision.
# if no "ndigits" used, it returns nearest int

round(12.6867)  # 13
round(12.6867, 2)   # 12.69




# Example 1: find the Greatest Magnitude
    # To find the greatest magnitude (the greatest distance from 0), I combine max() and abs()
    # I call abs() on each num, and find the maximum resulting value using max()

def max_magnitude(nums):
    return max(abs(num) for num in nums)

print(max_magnitude([2, 5, -78]))   # 78




# Example 2: Sum the Even Values 
    # I define a function called sum_even_values  which accepts any number of arguments, thanks to *args 
    # I grab the even numbers using the 'GENERATOR EXPRESSION' (arg for arg in args if arg % 2 == 0)  (could also use a list comp)
    # I pass the even numbers I extracted into sum()  and return the value
    # The default start value of sum()  is 0, so I don't have to do anything special to get it to return 0 if there are no even numbers!

def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

print(sum_even_values(1,3,4,7,8,9)) # 12




# Example 3: Sum Floats numbers
    # Write a function called sum_floats. This function should accept a variable number of arguments. 
    # The function should return the sum of all the parameters that are floats. 
    # If there are no floats the function should return 0

    # I started by defining sum_floats , which accepts any number of arguments using *args 
    # Much like the previous exercise, I use a 'generator expression' to extract the values in args where type()  is float.
    # I pass those values in to sum  and return the result

def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)        

print(sum_floats(12.4, 6, 7, 4.6))  # 17.0

