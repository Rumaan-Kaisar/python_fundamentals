
# Courses: colt_py_bootcamps    242

# ---------------    Class attribute and Class Methods    ---------------

# Previously we've seen 'Instance Attributes' and 'Instance Methods'

# Now we'll see 'Class Attributes' and 'Class Methods'
    # these kind not oftenly used


# Class Attributes:
    # We can also define attributes directly on a class that are shared by all instances of a class and the class itself.
    # "self" is not used in "Class Attributes", just directly define the attribute
    # We can access the attribule by directly using the Class-Name (also by object-instance)
    # generaly defined outside the class-methods or instance-methods
    

# A User class with both a class attribute. "active_users" is a class attribute
class User:

	active_users = 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"




print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(User.active_users)

print(user2.logout())
print(User.active_users)




# ----------------    use class attributes for VALIDATION    ----------------
# Another class with a class attribute, used for validation purposes.
# following code will only allowed for 'cat', 'dog', 'fish', 'rat'

class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat']

	def __init__(self, name, species):
		if species not in self.allowed:
            # self.allowed also works
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self, species):
		if species not in self.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat_1 = Pet("Blue", "cat")
dog_1 = Pet("Wyatt", "dog")

# tiger_1 = Pet("Miaw", "tiger")  # throws ERR

print(Pet.allowed)
Pet.allowed.append("Pig")

print(Pet.allowed)
cat_1.set_species("Pig")

print(cat_1.species)


# Class and its all Instance have this allowed attribute now.
# But they are different, and having Different Id's

print(Pet.allowed)		# ['cat', 'dog', 'fish', 'rat', 'Pig']
print(dog_1.allowed)    # ['cat', 'dog', 'fish', 'rat', 'Pig']
print(cat_1.allowed)    # ['cat', 'dog', 'fish', 'rat', 'Pig']

Pet.allowed.remove("fish") 
dog_1.allowed.remove("cat") 
cat_1.allowed.remove("dog") 

print(Pet.allowed)      # ['rat', 'Pig']		
print(dog_1.allowed)        # ['rat', 'Pig']
print(cat_1.allowed)        # ['rat', 'Pig']

print(id(cat_1.allowed))    # 2076059160832
print(id(Pet.allowed))   	# 2076059160832	
print(id(dog_1.allowed))    # 2076059160832  
print(id(cat_1.allowed))    # 2076059160832


# actually there is no difference between "Pet.allowed" and "self.allowed"
# They all refers to same ID. To change taht we need a Explicit change
cat_1.allowed = ["a", "b"]
print(id(cat_1.allowed))    # 2076063642048
print(cat_1.allowed)    # ['a', 'b'] 




# Example 1: Chicken Coop Exercise. following is implementation of the Chicken class.  
# Notice the total_eggs class attribute.

class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
    
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs

