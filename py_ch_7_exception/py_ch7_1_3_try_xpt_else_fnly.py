
# Courses: colt_py_bootcamps    210, 211

# Raised ERR or any ERR abruptly ends a program 
# however we can prevent abrupt ending by 'Handling ERR'

# Tell Python what to do if an ERR occurs

# ------------------    try & except    ------------------
foober      # ERR: Name ERR

try:
    foobar
except NameError as err:
    print(err)
print("After try/extept")


# More Generally we can catch all ERR, if we do not specify it.
try:
    foobar
except:
    print("Problem")

# Above is GENERIC and catch all sort of ERR. 
	# However it is not a good idea if we don't explain the Error

# What we are doing here is catching every error, 
	# which means we are not able to correctly identify "what" went wrong. 
	# It is highly discouraged to do this.




# Example 1: following demonstrates try-except mechanism
def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

dct_1 = {"a": 23, "c": 45, "x": 67}

dct_1["d"]   # ERR: Key Error, pgram stops abruptly
print("after err")

get(dct_1, "d")     # Handling ERR
print("after err")

get(dct_1, "a")
print("after execution")


''' 

def get(d,key):
    	try:
		return d[key]
	except KeyError:
		return None
d = {"name": "Ricky"}
print(get(d, "city"))
d["city"]

 '''

# python py_ch7_1_3_try_xpt_else_fnly.py 

