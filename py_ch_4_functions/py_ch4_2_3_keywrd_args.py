# Courses: colt_py_bootcamps    158, 


# -------------|    Keyword Arguments    |-------------
    # Previously we've seen order in function parameters are important
    # However order doesn't matter if we use "Keyword Arguments"
    # specify funtion parameters "Keyword" with "arguments" while calling the function


def full_name(first = "Joshua", last = "Benjio"):
    return f"Your name is {first} {last}"

# -------------|    order doesn't matter   |-------------
print(full_name(first = "Ian", last = "Goofellow"))
print(full_name(last = "Black", first= "Adam"))

# Following two are DIFFERENT but looks SAME
    # during definition "def full_name(first = "Joshua", last = "Benjio"):"   specifies the defaul values
    # during calliong "full_name(first = "Ian", last = "Goofellow")" using "Keyword Arguments"


def exponent(num, power=2):
	return num ** power

# Order doesn't matter anymore, if we use key word arguments:
print(exponent(num=2,power=3)) #8
print(exponent(power=3, num=2)) #8

# Without keywords args, order still matters:
print(exponent(3,4)) #81
print(exponent(4,3)) #64


# Usefull:
    # More explicit and readable.
    # Used for passing a dictionary to a function, and unpacking its values









