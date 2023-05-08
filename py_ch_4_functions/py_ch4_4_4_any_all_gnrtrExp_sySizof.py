
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
