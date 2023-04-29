
# Courses: colt_py_bootcamps    175, 176

# =================    variable arguments. Var Args    =================

# ----------|    single star * operator : *args   |----------
    # A special operator we can pass to functions as a parameter
    # It Gathers remaining arguments as a tuple, we named this tuple "args"
    # "args" in *args is just a parameter - you can call it whatever you want! But the * must be present

# function WITHOUT *args
def sum_all_nums(num1, num2, num3):
    return num1+num2+num3

print(sum_all_nums(4, 6, 91))   # 101

# We cannot use 4 or 5 inputs in above function. We have to code it.
    # to make variable arguments we need to set default values 
def sum_all_nums(num1, num2, num3=0, num4=0, num5=0):
    return num1 + num2 + num3 + num4 + num5

print(sum_all_nums(1, 2, 3, 4, 5))


# To input any number of arguments we can use *args. 
def sum_args(*num_args):
    print(num_args)
    total = 0
    for nums in num_args:
        total += nums
    return total

print(sum_args(1, 2, 3, 4, 5))
print(sum_args(1, 2, 3))

# we can put parameters before the *args, *args are consitered as a TUPLE
# following prints first two arguments and sums the rest
def sum_args(num1, num2, *num_args):
    print(num1)
    print(num2)
    print(num_args)
    total = 0
    for nums in num_args:
        total += nums
    return total


print(sum_args(1, 2, 3, 4, 5))
print(sum_args(1, 2, 3))



# Example 1:
def feed_me(*stuff):
    for thing in stuff:
        print(f"YUMMY I EAT {thing}")
feed_me("apple", "tire", "shoe", "salmon")



# Example 2:
def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Note sure who you are"

print(ensure_correct_info("hello", False, 78)) # Not sure who you are...

print(ensure_correct_info(1, True, "Steele", "Colt"))



# Example 3:
    # Don't need to write the else  part of the conditional in this case, because I'm returning out of the function on the line before. 
    # So the only way the return False  line runs is if the above line didn't run.  It's an implicit else .

def contains_purple(*args):
    if "purple" in args: return True
    return False

contains_purple(6, 7, "purple")