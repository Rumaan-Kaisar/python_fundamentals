
# Courses: colt_py_bootcamps    254, 255

# -----------------    property    -----------------
class Human:
    def __init__(self, first, last, age) :
        self.first = first 
        self.last = last 
        self.age = age


jane = Human("Jane", "Goodall", 50) 
print(jane.age) 
jane.age = -100     # setting a negative age
print(jane.age) 




# Applying condition
# We can prevent -ve age by adding a condition
class Human:
	def __init__(self, first, last, age) :
		self.first = first 
		self.last = last 
		self.age = age
		# self.age = max(age, 0)  # will also work
		if age >= 0 :
			self.age = age
		else:
			self.age = 0

# Now, above will prevent setting -ve value
jane = Human("Jane", "Goodall", -9)
print(jane.age)




# -------------------    GET-SET interface    -------------------
# We can far more modify it, by making a GET-SET interface
class Human:
    def __init__(self, first, last, age) :
        self.first = first 
        self.last = last 
        self.age = age

        # notice we made it PRIVATE
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # ------    acessing and changing age (GET-SET)    -----------
    # shows the current age
    def get_age(self):
        return self._age

    # set a new age
    def set_age(self, new_age): 
        if new_age >= 0: 
            self._age = new_age
        else:
            self._age = 0


jane = Human("Jane", "Goodall", -9) 
print(jane.get_age()) # 0
jane.set_age(45) 
print(jane.get_age())   # 45




# ----------     Adding property: GETTER-SETTER     ------------
# there is no real GETTER-SETTER in python, its just a SYNTACTIC SUGAR
# We can use property to do above work
class Human:
    def __init__(self, first, last, age) :
        self.first = first 
        self.last = last 
        self.age = age

        # notice we made it PRIVATE
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # # ------    acessing and changing age (GET-SET)    -----------
    # # shows the current age
    # def get_age(self):
    #     return self._age

    # # set a new age
    # def set_age(self, new_age): 
    #     if new_age >= 0: 
    #         self._age = new_age
    #     else:
    #         self._age = 0

    # -----------    GETTER & SETTER    -----------
    # By using DECORATORS we can call following methods without "()"
    @property # this act is "GETTER": it simply shows/gets the value
    def age(self):
        return self._age

    @age.setter     # this act is "SETTER"
    def age(self, value): 
        if value >= 0: 
            self._age = value
        else:
            raise ValueError("age can't be negative!")

    # Not for both GETTER and SETTER the method_name "age" should be the same


    # following is another Example of GETTER-SETTER
    @property 
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter 
    def full_name(self, name): 
        self.first, self.last = name.split(" ")



# jane = Human("Jane", "Goodall", -9) 
jane = Human("Jane", "Goodall", 29) 
# print(jane.get_age()) 
# jane.set_age(45) 
# print(jane.get_age())

# ----------    impact of DECORATOR    ----------
# folowing we are actually calling the GETTER, not the "age" variable
# Decorators altered the behaviour of a method, we don't need "()" any more
    # we just call the method "age()" without () like an attribute

# Note that: we are invoking GETTER and SETTER by only using "age"    
  #  we don't need to call them seperately as we did for "get_age() & set_age()" 
print(jane.age) # invokes GETTER
jane.age = 20   # invokes SETTER
print(jane.age) # invokes GETTER

# another example of GETTER-SETTER
print(jane.full_name)   # invokes GETTER
jane.full_name = "Tim Minchin"  # invokes SETTER
print(jane.__dict__)





# -----------------    super    -----------------

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")



# without using super() or paraent.__init__()
class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        # duplication occurs (use inheritance to avoid this)
        self.name = name
        self.species = species
        self.breed = breed
        self.toy = toy

blue = Cat("Blue", "cat", "Scottish Fold", "String")
print(blue)


# using paraent.__init__()
class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		# paraent.__init__() to avoid duplication
		Animal.__init__(self, name, species)
		self.breed = breed
		self.toy = toy

blue = Cat("Blue", "cat", "Scottish Fold", "String")

print(blue)
print(blue.species) # using from BASE CLASS "Animal"
print(blue.breed) 	# using from CHILD CLASS "Cat"
print (blue.toy)	# using from CHILD CLASS "Cat"




# Inheritance Example Using -------    Super()    ---------
    # it is similar to using paraent.__init__(), but we dont need to specify "self"
    # super() refers to immidiate parent (which is passed in the argument od CHILD)
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


# using super()
class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue","Scottish Fold", "String")

print(blue)
print(blue.species) # using from BASE CLASS "Animal"
print(blue.breed) 	# using from CHILD CLASS "Cat"
print (blue.toy)	# using from CHILD CLASS "Cat"

blue.play()

