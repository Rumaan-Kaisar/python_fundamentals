
# Courses: colt_py_bootcamps    180, 181

# -------------    Problem passing List/Tuple to *args    -------------
    # Using * as an Argument (during function call): Argument Unpacking
    # We can use * as an argument to a function-call to "unpack" values like "List" or "Tuple"

def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

# sum_all_values(1,30,2,5,6)
    # args: (1, 30, 2, 5, 6)

# following returns ERROR
nums = [1,2,3,4,5,6]
sum_all_values(nums)    # ERROR
    # args: ([1, 2, 3, 4, 5, 6],), list is stored as an element of the *args tuple

# -----------    unpacking list    -----------
# to unpack the list and pass its elemens as individual arguments to *args, we need to use '*' in the function call
sum_all_values(*nums)   # works
    # args: (1, 30, 2, 5, 6)


# -----------    unpacking Tuple    -----------
# following also returns ERROR
nums2 = (1,2,3,4)
sum_all_values(nums2)    # ERROR
#  args: ((1, 2, 3, 4),) tuple is stored as an element of the *args tuple
sum_all_values(*nums2)   # works




# Example 1: Simple Unpacking Exercise Solution
# Here's what you were given:

def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

# First, call count_sevens  with the numbers: 1,4, and 7  (review)
result1 = count_sevens(1,4,7)

# Next, call count_sevens  with all the values from the "nums"  list, unpacked:

result2 = count_sevens(*nums)
# Adding that little '*'  makes a huge difference! Instead of passing in a single item (the list), we're now passing in 121 separate arguments.


