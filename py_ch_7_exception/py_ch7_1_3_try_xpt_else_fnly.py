
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


# More Generally we can catch all ERR, if we not specify it.
try:
    foobar
except:
    print("Problem")

# Above is generic and catch all sort of ERR. 
# However it not a good idea if we dont explain the Error

# What we are doing here is catching every error, 
#     which means we are not able to correctly identify "what" went wrong. 
#     It is highly discouraged to do this.




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




# ------------------    else & finally    ------------------
    # if "try" fails "except" will executed
    # if "try" success "else" will executed
    # "finally" always executed

try:
	nm =int(input("please Enter a number : "))
except:
	print("Thats not a number")
else:
	print("I'm in ELSE !!")
finally:
	print("runs no matter what")
	



# Example 2: Runs untill a number is entered (use it in the Guessing Game)
while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("Good job, you entered a number!")
		break
	finally:
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")




# ------------------    Catching Multiple ERR    ------------------

# Example 3: Handle a ZeroDivisionError in math division
def divide(a,b):
    try: 
        result = int(a)/int(b)
    except ZeroDivisionError:
        print("don't divide by zero please!")
    except ValueError:
        print("Use a valid number!!")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")


a = input("please enter a number: ")
b = input("please enter a number: ")

print(divide(a, b))




# Example 4: We'll catch multiple ERR: ZeroDivisionError, TypeError, ValueError by COMBINING them
def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError, ValueError) as err:
		print("Something went wrong!")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")

# print(divide(1,2))
print(divide(1,'a'))
print(divide(1,0))




# Example 5: Here's another version of the divide function:

def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total


# python py_ch7_1_3_try_xpt_else_fnly.py 
