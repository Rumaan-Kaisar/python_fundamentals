
# Courses: colt_py_bootcamps    245, 246, 247


# ------------------    class method    ------------------
# Class methods are methods (with the @classmethod decorator, decorator is kind of syntactic sugar) 
    # that are not concerned with instances, but the class itself.
        # INSTANCE METHODS always used
        # CLASS METHODS are rarely used

# Demo of a class method
class Person(): 
    # . . .

    @classmethod
    def from_csv(cls, filename):
        return cls(*params)     # this is the same as calling Person(*params) 

Person.from_csv(my_csv)




# Example 1: A User class with both instance attributes and instance methods
class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):  # we can use "self", no difference.
        # Convension: "cls" used to signify that we're working with class, not instance 
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

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



user1 = User("Joe", "Smith", 68)
user2 = User("Joe", "Smith", 68)

# both prints the same result
print(User.display_active_users())
print(user1.display_active_users())

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_users())



tom = User.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())




# ------------------    __repr__    ------------------

class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1
	# NEW CODE
	def __repr__(self):
		return f"{self.first} is {self.age}"
	# NEW CODE


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


tom = User.from_string("Tom,Jones,89")

j = User("judy", "steele", 18)
j = str(j)
print(j)
















