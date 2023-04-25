
# Courses: colt_py_bootcamps    159,   

# ------------    Scope of a function    ------------
# access of variables, local & global

# variables created inside of a function destroyed when function exit

# Global scope:
tmpl = "Temp"

def use_temp():
    return f"{tmpl} is used"

print(use_temp())

# localal scope:
def use_nm():
    name = "Solo"
    return f"Hi {name}, local is used"

print(use_nm())
# print(name)




# Cannot access global variable inside of a function.
# Any variable inside a function are cosidered local
# use "global" keyword
    # this problem arise, when we want to change a "global" variable from "inside" of a function
    # don't need "global" if we just use the global value.
tmpl2 = "Temp"

def use_temp_2():
    # tmpl2 += " For templates"   # gives ERR
    global tmpl2    # interpretor will look for a "global" variable instead of "local"
    tmpl2 += " For templates"    # use "global" keyword
    return tmpl2

print(use_temp_2())




# ------------    nonlocal keyword    ------------
# Lest us modify a parent-functions variable in a child (nested) function
def outer():
    count = 0

    def inner():
        nonlocal count 
        count += 1
        return count
    
    return inner()

print(outer())

