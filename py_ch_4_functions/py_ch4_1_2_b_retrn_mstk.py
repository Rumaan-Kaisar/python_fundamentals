
# Courses: colt_py_bootcamps    155 

# ------------|    Common Return Mistakes     |------------

# Example 1: Proper indentation of return
def sum_odd_nums(nums):
    sum = 0
    for num in nums:
        if num%2 != 0:
            sum += num
    return sum



# Example 2: Avoid unnecessary "else"
def is_odd_num(num):
    if num%2 != 0:
        return True
    else:
        return False

# can be re-written as:
def is_odd_num(num):
    if num%2 != 0:
        return True
    return False

print(is_odd_num(9))
print(is_odd_num(4))




# Example 3: Here's the initial broken state of the function, fix by proper indentation

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        return count

# The problem is that the function returns the very first time through the loop 
    # because of the way return is indented.

# To fix it, all we have to do is outdent the return statement 
    # so that it now only returns after the loop finishes running


def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count