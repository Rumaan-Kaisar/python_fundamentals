# Courses: colt_py_bootcamps    152, 153


# Example 1: basic syntax
def sqr_nm(num):
    return num*num

print(sqr_nm(4))
print(sqr_nm(8))


# Example 2: Another simple function
def sing_happy_birthday(name):
    print("Happy Birthday To You") 
    print("Happy Birthday To You") 
    print(f"Happy Birthday Dear '{name}!'") 
    print("Happy Birthday To You")

sing_happy_birthday("SaNdars")



# Example 3: multi parameters
def print_full_name(first_name, last_name):
    print(f" your name is {first_name}  {last_name}")

print_full_name("Andy", "Volok")

# ---------------    parameters & arguments    ---------------
# in above code first_name, last_name are "parameters" but "Andy", "Volok" are arguments


# Example 4: following are various parametarized functions, that uppercase the letters.

    # Using string concatenation:
def yell(word):
    return word.upper() + "!"

yell("word")


    # Using the string format() method:
def yell(word):
    return "{}!".format(word.upper())

yell("bobob")


    # Using an f-string.
def yell(word):
    return f"{word.upper()}!"

yell("bon bon")




# Example 5: Keep track of the days in a list.  
    # Check to make sure num isn't < 0 or  > 6.  
    # Return the corresponding day. Use 'days[num-1]' because 'return_day(1)' should return 0th item in list.

def return_day(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

# BONUS ADVANCED VERSION:
    # Here's a more advanced solution that involves error handling, which we have not covered yet.  
    # It eliminates the need to check to see if num is a 'valid index' in the list.

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

    
