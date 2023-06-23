
# Courses: colt_py_bootcamps    261, 262, 263

# ----------------    Polymorphism    ----------------
# A key principle in OOP is the idea of polymorphism - an object many (poly) forms (morph).

# 1. The 'same class method' works in a similar way for different classes

    # ----------------    METHOD OVERRIDING    ----------------

    # A common implementation of this is to: 
        # METHOD OVERRIDING: Have a method in a base (or parent) class that is overridden by a subclass. 
            # This is called method overriding.
        # Each subclass will have a different implementation of the method.
            # If the method is not implemented in the subclass, the version in the parent class is called instead.

class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal): 
    def speak(self): 
        return "woof"

class Cat(Animal): 
    def speak(self):
        return "meow"

class Fish(Animal): 
    pass       

class Human(Animal): 
    def speak(self):
        return "yo"

# Cat.speak()	    # meow
# Dog.speak()	    # woof
# Human.speak()	# yo

d = Dog()
print(d.speak())

f = Fish()
print(f.speak())




# 2. The 'same operation' works for different kinds of objects
sample_list = [1,2,3]
sample_tuple = (1,2,3) 
sample_string = "awesome"
# noticew the len() method works for all list, tuple, strings
len(sample_list) 
len(sample_tuple) 
len(sample_string)


# -----------------    special methods: operator overloading    --------------------
# How does the following work in Python?
8+2         # 10 : addition
"8" + "2" #  82 : concatenation

# Python classes have special (also known as "magic") methods, that are "DUNDERS" (i.e. double underscore-named).
    # These are methods with special names that give instructions to Python for how to deal with objects.
        # length, string-reperesentation, how object of a class are multiplied or added
    
