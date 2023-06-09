
# Courses: colt_py_bootcamps    242

# ---------------    Class attribute and Class Methods    ---------------

# Previously we've seen 'Instance Attributes' and 'Instance Methods'

# Now we'll see 'Class Attributes' and 'Class Methods'
    # these kind not oftenly used


# Class Attributes:
    # We can also define attributes directly on a class that are shared by all instances of a class and the class itself.
    # "self" is not used in "Class Attributes", just directly define the attribute
    # We can access the attribule by directly using the Class-Name (also by object-instance)
    

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
# following code will only allowed for

class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat']

	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")






# Example 1: Chicken Coop Exercise.
Here's my implementation of the Chicken class.  Notice the total_eggs class attribute.



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

