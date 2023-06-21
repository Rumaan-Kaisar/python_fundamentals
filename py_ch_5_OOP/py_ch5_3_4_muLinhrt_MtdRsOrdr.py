
# Courses: colt_py_bootcamps    258, 259

# ------------    Multiple inheritance    ------------

from xml.dom import HierarchyRequestErr


class Aquatic:
  def __init__(self,name):
    print("AQUATIC INIT!")
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"



class Ambulatory:
  def __init__(self,name):
    print("AMBULATORY INIT!")
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"


# Ineherit from two different classes 
  # just specify the parent classes in the argument
  # Ambulatory, Aquatic are two different classes they have no relation
  # But "Penguin" has relation to both classes

# class Penguin(Aquatic, Ambulatory):
class Penguin(Ambulatory, Aquatic):  
  def __init__(self,name):
    print("PENGUIN INIT!")
    # Aquatic's __init__() never caled if super().__init__ is ussed
      # But because of the inheritance we have acces to the other methods of both parent classes
    super().__init__(name=name) # if class is unspecified MRO applied

    # for the above reason we can explicitky call the __init__ of each parent calsses
      # However "greet" is invoked from "Ambulatory"
    # Ambulatory.__init__(self,name=name)
    # Aquatic.__init__(self, name=name)



jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
# note that when class_name is unspecified and super().__init__ is used
  # first of the specified base's method will be used (in case both class has same method_name)
  # i.e Aquatic, Ambulatory both has "greet()"
    # in case of "class Penguin(Aquatic, Ambulatory)" Aquatic's "greet" wil be used
    # in case of "class Penguin(Ambulatory, Aquatic)" Ambulatory's "greet" wil be used
print(captain_cook.greet())

# followig shows "captain_cook" is the instance of all three classes 'Penguin', 'Aquatic' and 'Ambulatory'
print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")


# jaws.swim() # 'Jaws is swimming'
# jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
# jaws.greet() # 'I am Jaws of the sea!'

# lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
# lassie.walk() # 'Lassie is walking'
# lassie.greet() # 'I am Lassie of the land!'

# captain_cook.swim() # 'Captain Cook is swimming'
# captain_cook.walk() # 'Captain Cook is walking'
# captain_cook.greet() # ??





# --------------------         MRO : Method Resolution Order         --------------------
# "Penguin" inherits from both "Aquatic" and "Ambulatory", therefore instances of Penguin can call both the walk and swim methods.
  # What about the "greet" method for our instance of Penguin(Aquatic , Ambulatory)? It is calling the 
    #     Aquatic.greet() 
    #                     instead of 
    #     Ambulatory.greet().

# How is the oreder established


# MRO:
  # Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class, 
  # which is the order in which Python will look for methods on instances of that class.

  # It's like a Hierarchy:
    # the rule is changed from Python 2.x to 3.x


# There are 3 different ways to access and see the MRO for a given class
      # __mro__ : There is __mro__ attribute on a class
      # mro(): use the "mro()" method on the class (same result as __mro__)
      # help(cls): RECOMENDED. Use the built in "help(cls)" method. It more human readable


# Example: 
Penguin.__mro__
#	(<class 'multiple.Penguin'>, <class 'multiple.Aquatic'>,
#	<class 'multiple.Ambulatory’>, <class 'object’>)

Penguin.mro()
#	[ __main__.Penguin, __main__.Aquatic, __main__.Ambulatory, object]

help(Penguin) # best for HUMAN readability -> gives us a detailed chain



# ---------    MRO: Explanation    ---------
class A:
  def do_something(self):
    print("Method Defined In: A")

class B(A):
  def do_something(self):
    print("Method Defined In: B")

class C(A):
  def do_something(self):
    print("Method Defined In: C")

class D(B,C):
  def do_something(self):
    print("Method Defined In: D")


thing = D()
thing.do_something()
 

# Chain of the above class be like
        #     A
        #   /  \
        #   B  C
        #   \ /
        #    D



# ----------    Testing MRO    ----------

class A:
  def do_something(self):
    print("Method Defined In: A")

class B(A):
    pass
#   def do_something(self):
#     print("Method Defined In: B")

class C(A):
  def do_something(self):
    print("Method Defined In: C")

class D(B,C):
    pass
#   def do_something(self):
#     print("Method Defined In: D")


thing = D()
thing.do_something()    # Method Defined In: D
 

# Chain of the above class be like
        #     A
        #   /  \
        #   B  C
        #   \ /
        #    D

    # MRO - hierarchy (using "mro()"):   
        # D, B, C, A, objects


# D is defined as below
class D(B,C):
    pass

# then following will print: "Method Defined In: B"
thing = D()
thing.do_something()


# Again if B is defined as below
class B(A):
    pass

# then following will print: "Method Defined In: C"
thing = D()
thing.do_something()


# To find out MRO of the class:
print(D.__mro__)

# following also gives same result
print(D.mro())

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    # Shows us it has the hierarchy: 
        # D
        # B
        # C
        # A


# following gives more "HUMAN READABLE" format
help(D)

""" 
    Help on class D in module __main__:

    class D(B, C)
    |  Method resolution order:
    |      D
    |      B
    |      C
    |      A
    |      builtins.object
    |
    |  Methods inherited from B:
    |
    |  do_something(self)
    |
    |  ----------------------------------------------------------------------
    |  Data descriptors inherited from A:
    |
    |  __dict__
    |      dictionary for instance variables (if defined)
    |
    |  __weakref__
    |      list of weak references to the object (if defined)
"""


# python py_ch5_3_4_muLinhrt_MtdRsOrdr.py

 
