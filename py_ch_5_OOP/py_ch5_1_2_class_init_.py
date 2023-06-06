# Courses: colt_py_bootcamps    235, 237


# ------------------    class definition    ------------------
# Convention: Always use "CamelCase" first letter in uppercase
# use snake_case for "variables" and "functions"

class Person:
	pass    # Empty class are not valid in python, so we used "pass"

p = Person()    # use () to create an 'Instance' of a class
print(type(p))
print(p)




# Example 1: Define a class called Vehicle.  It should be completely empty (just add a pass statement inside) . 
                # After the class is defined, create two instances of Vehicle.  
                    # Save one to a variable called car  
                    # Save another to a variable called boat.

class Vehicle:
    pass

car = Vehicle()
boat = Vehicle()

print(type(car))   # <class '__main__.Vehicle'>
print(car)         # <__main__.Vehicle object at 0x000001A969FF7D00>





# ------------------    _ _init_ _    ------------------
# Adding attributes to our classes

# Anytime we create a class and want to use it, Python always looks for __init__(),
# Classes in Python can have a special __init__() method, 
    # which gets called every time you create an instance of the class (instantiate).  
    # It initialize the class, if we dont use it, Python will create default __init__() 

class Vehicle:
    def __init__(self, make, model, year):
        print("Anew class is created")
        self.make = make 
        self.model = model 
        self.year = year

# __init__() autometically called
boat = Vehicle("wood", "unknown", "1935")
train = Vehicle("iron", "LOCO1337x", "1850")
car = Vehicle("plastic", "unknown", "2001")
v = Vehicle("Honda", "Civic", 2017)
""" 
    v
    <__main__.Vehicle object at 0x000001A969FF7D00>
    v.make 
        'Honda' 
    v.model 
        'Civic' 
    v. year 
        2017
"""




# --------------    self    --------------
    # The self keyword refers to the current class instance.
    # self must always be the first parameter to _init_ 
    # any methods and properties on class instances are defined with "self"

# Remember, the parameter doesn't have to be called "self", but it is the STANDARD and pretty much the only thing you'll see




# Example 2: Create a user class
class User:
    def __init__(self, first, last, age):
        self.first_name = first   # creating a varibale "name" and giving value of "first"
        self.last_name = last
        self.person_age = age


user_1	= User("Joe", "Smith", 68)
user_2	= User("Blanca", "Lopez", 41)
print(user_1.first_name, user_1.last_name) 
print(user_2. first_name, user_2.last_name)
