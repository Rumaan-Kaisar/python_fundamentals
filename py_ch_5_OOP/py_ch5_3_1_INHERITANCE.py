
# Courses: colt_py_bootcamps    253

# ------------------    INHERITANCE    ------------------

# OBJECTIVES
    # Implement inheritance, including "multiple-inheritance"
    # Understand MRO-"Method Resolution Order" 
    # Understand polymorphism 
    # Add special methods to classes



# Inheritance:
    # It's A key feature of OOP is the ability to define a class which inherits from another class (a "BASE" or "PARENT" class).
        # for example in cas eof website: Admin , Moderator and user. 
            # "Admin" has all funtionality of "user" and a "moderator" but it has some extra funtionality.
            # we can say "Admin" inherits from "Moderator" and "moderator" inherits from "user".

    # In Python, inheritance works by passing the "PARENT" class as an "argument" to the 'definition of a child class':



# Demo of INHERITANCE
class Animal:
    def make_sound(self, sound): 
        print(f"this animal says {sound}")

    cool = True

# Cat class inherits from Animal
class Cat(Animal):  # Notice PARENT-"Animal" class as an "argument"
    pass
    # this class doesn't define anything but it "inherits" all methods from its parent class


gandalf = Cat()

# following is possible because of "INHERITANCE"
gandalf.make_sound("meow")	# meow
gandalf.cool # True


# Make a new cat instance
blue = Cat()

# Because of inheritance, a Cat has access to:
blue.make_sound("Meow Miu")
print(blue.cool)
print(Cat.cool)
print(Animal.cool)
print(gandalf.cool)


#blue is both a Cat and Animal (and base object)
print(isinstance(blue, Cat))
print(isinstance(blue, Animal))
print(isinstance(gandalf, Animal))
print(isinstance(blue, object))


# isinstance():
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.

# python py_ch5_3_0_row.py