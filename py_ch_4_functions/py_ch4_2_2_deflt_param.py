# Courses: colt_py_bootcamps    156, 157

# -----------|    Default Params    |-----------
# Giving parameters default values
    # Helps to avoid Errors
    # More flexiblity
    # defaul parameters can be anything: function, lists, dictionaries, strings, booleans

def sqr(nm, pow = 2):
    return nm**pow

# If second argument is not present, default value of pow = 2 is used
print(sqr(4))
print(sqr(8))
print(sqr(8, 4))


def add(a = 0, b = 0):
    return a + b

def subtract(a = 0, b = 0):
    return a - b

def multiply(a = 0, b = 0):
    return a * b

print(add(8, 4))
print(add())



# use function as default parameters
    # Note that, the parameters are has to be inn order
def math_a(a = 0, b = 0, fn = add):
    return fn(a, b)

print(math_a())
print(math_a(2, 2))
print(math_a(2 ,2, subtract))




# Instructors versions
# exponent
def exponent(num, power=2):
	return num ** power

print(exponent(2,3)) #8
print(exponent(3)) #9
print(exponent(7)) #49


# math
def add(a,b):
    return a+b

def math(a,b,fn=add):
    return fn(a,b)

def subtract(a,b):
    return a-b

print(math(4,5)) #results in add(4,5) which is 9

print(math(4,5,subtract)) #results in subtract(4,5) which is -1



# ------------    Exercise    ----------
# The most straight forward solution is to use a large if-elif-else statement:

def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"


# Another shorter solution involves using a dictionary that maps animal names to noises.
noises = {
    "dog": "woof", 
    "pig": "oink", 
    "duck": "quack", 
    "cat": "meow"
}

# Then, we just use the dictionary.get() method to retrieve the correct animal noise and save it to a variable called noise. 
    # get() will return None  if the animal is not in the dictionary.  
    # Then we just check to see if noise  exists.  If it does, return noise .  Otherwise, return "?" 

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"



# More compact solution which passes in a default value to get()
def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')


