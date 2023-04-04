# Courses: colt_py_bootcamps    97, 98, 100

""" 
    Lists are one of 4 built-in data types in Python used to store collections of data, 
        the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage. 
"""

# Lists are created using square brackets []
    # List are :
    # Ordered
    # Changable
    # allow duplicate values

# simple list
thislist = ["apple", "banana", "cherry", "apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List items can be of any data type, it can contain different data types
list1 = ["abc", 34, True, 40, "male"]

# Define my_stuff
my_stuff = [1, 2, 3, 4, "Camera", 2.5]

# list() Constructor: It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# ------------|    List Length    |------------
# To determine how many items a list has, use the len() function
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# ------------|    Converting/Turning a 'sequence' into a 'list'    |------------
r = range(1, 11)
r_list = list(r)
print(r_list)

# Define a list of numbers called 'nums'
nums = list(range(1,100))


#  ------------|    Accessing list items    |------------
""" 
        -ve values to count from last item.
            0       1           2
        ["apple", "banana", "cherry"]
            -3      -2          -1 
"""
thislist = ["apple", "banana", "cherry"]
print(len(thislist[2])) # cherry
print(len(thislist[-1])) # cherry

# Check a value in a list
"apple" in thislist     # true
"mango" in thislist     # false
print(f"{'apple' in thislist} and {'mango' in thislist}")
# so we can use it as a condition:
if "apple" in thislist:
    print("apple is on us")
