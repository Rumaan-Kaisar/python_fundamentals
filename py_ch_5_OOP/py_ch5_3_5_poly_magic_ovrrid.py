
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
    



# Example 1: Special method behind "+"
    # What is happening in our example?
8+2         # 10 : addition
"8" + "2" #  82 : concatenation

# The + operator is shorthand for a special method called __add__() that gets called on the first operand.
    # If the first (left) operand is an instance of int, __add__() does mathematical addition. 
    # If it's a string, it does string concatenation.




# Example 2: Special Methods Applied
# Therefore, you can declare special methods on your own classes to 
    # mimic the behavior of builtin objects, like so using __len__:
class Human:
    def  __init__ (self, height):
        self.height = height # in inches

    def  __len__ (self):
        return self.height


mougli = Human(60) 
print(len(mougli)) # 60    

# __repr__ is also a special method
# The __repr__ method is one of several ways to provide a nicer string representation:
class Human:
    def  __init__ (self, name="somebody"):
        self.name = name

    def  __repr__ (self):
        return splf.name

dude = Human()
print(dude) # "somebody”


# there are many more "special functions"
# some commonly used are: __int__, __new__, __add__, __len__, and __str__ 




# Example 3: Here is another example
import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last 
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first ='Newborn', last = self.last, age = 0)
        return "You can't add that"

    def __mul__(self, other):
        print("You are multiplying humans")
        if isinstance(other, int):
            # return [self for i in range(other)]     # not creating actual copies, refer to same obj
            return [copy.copy(self) for i in range(other)]
        return "You can't multiply"


j = Human("Jenny", "Larsen", 47) 
k = Human("Kevin", "Jones", 49) 
print(j) 
print(len(j))

print(k) 
print(len(k))

y = j + k
print(y)

print(j * 2)    # You are multiplying humans




# --------------    ORDER of the operands matters     --------------
print(j * 2)    # invokes the __add__() defined in the Human class
# print(2 * j)    # invokes the "integer version" of __add__() 
print(j * "a")   # You can't multiply


# Notice the following problem:
    # we just changed the one element of the list, but all are changed

triplets = j * 3 
triplets[1].first = 'Jessica' # changing the second element 
print(triplets)
# [Human named Jessica Larsen aged 47, Human named Jessica Larsen aged 47, Human named Jessica Larsen aged 47]



# -----------    copy module    ------------
# This is happening because we are not actuale made 3-copies of the object 3
    # These 3 elements refers to same object and they are linked
    # to make the actual seperate copies of the object we use "copy" module

# copy module:
import copy
# from copy import copy

# then use the following code
# return [copy.copy(self) for i in range(other)]

# [Human named Jenny Larsen aged 47, Human named Jessica Larsen aged 47, Human named Jenny Larsen aged 47]



# ------------    combine DUNDERs    -------------
# we can now "COMBINE" the special methods
triplets_2 = (j + k) * 3
print(triplets_2)





# ----------------    Use __dunder__ anlong with inheritance    ----------------

# Example 4: Notice how we create our own version of "Dictionary" called "GrumpyDict"
    # This "GrumpyDict" is a child of "dict" class 
    # "GrumpyDict" calles "dict" class's DUNDERs in its own DUNDER methods to make 
        # its own dictionary type methods
            # __missing__   for not found element
            # __setitem__   change a dictionary item
            # __contains__  check an item


class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"YOU WANT {key}?  WELL IT AINT HERE!")

	def __setitem__(self, key, value):
		print("YOU WANT TO CHANGE THE DICTIONARY?")
		print("OK FINE...")
		super().__setitem__(key, value)

	def __contains__(self, item):
		print("NO IT AINT IN HERE!")
		return False

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
'city' in data

