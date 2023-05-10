
# Courses: colt_py_bootcamps    190

# --------------    all : INTERSECTION    --------------
# Takes an iterable as an agumnet
# Return True if all elements of the iterable are truthy (or if the iterable is empty)
all([0, 1, 2, 3]) # False

all([char for char in 'eio' if char in 'aeiou'])    # True

all([num for num in [4, 2, 10, 6, 8] if num%2==0]) # True: Check all collected numbers are even




# Example 1: Find that all names starts with "C"
people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]

[name[0]=="C" for name in people]   # [True, True, True, True, True]
all([name[0]=="C" for name in people])  # True

people.append("Vikk")

[name[0]=="C" for name in people]   # [True, True, True, True, True, False]
[name[0]=="C" for name in people]  # False




# Example 2: Check all numbers are even
nums = [1, 4, 2, 10, 6, 8]
all([num%2==0 for num in nums]) # False




# --------------    any : UNION    --------------
# Return True if any element of the iterable is truthy. 
# If the iterable is empty, return False.

any([0, 1, 2, 3]) # True
any([val for val in [1,2,3] if val >2]) # True 
any([val for val in [1,2,3] if val >5]) # False




# Example 3: Check if any number is odd
numsAny = [1, 4, 2, 10, 6, 8]
any([num%2==0 for num in numsAny]) # True

# also check any numbe ris even
any([num%2==1 for num in numsAny]) # True




# --------------    Generator Expression    --------------
# No need to use list comprehension braces
numsAny = [1, 4, 2, 10, 6, 8]
# [num for num in numsAny if num%2==0]
any(num for num in numsAny if num%2==0)     # true

# Generator Expression
(num for num in numsAny if num%2==0)    # <generator object <genexpr> at 0x000001C6A4C49A10>
# 'generator object' is not a list, 
    # "LISTS" are havier than "generator object"
    # To save memory/space we'll use 'generator object' instead of list comprehension

# Basically, use a "generator expression" if all you're doing is "iterating once". 
# If you want to store and use the generated results, then you're probably better off with a list comprehension.


# Example 4: Memory usage Demo:
import sys
list_comp = sys.getsizeof([x*10 for x in range(1000)]) 
gen_exp = sys.getsizeof(x*10 for x in range(1000))

print('To do the same thing, it takes...') 
print( f'List Comprehension: {list_comp} bytes') # List Comprehension: 8856 bytes
print(f"Generator Expression: {gen_exp} bytes") # Generator Expression: 104 bytes


