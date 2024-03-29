# Courses: colt_py_bootcamps    256, 257

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


tom = User.from_string("Tom, Jones, 89")

j = User("judy", "steele", 18)
j = str(j)
print(j)


# -----------------          creating a child of above class          -----------------
# above is a code for a website-user
    # now we can define a class for website-moderator as a child of above class
    # if we didn't use inheritance to define "Moderator" the active user won't increment
        # because "User"s __init__ wont invoked.

class Moderator(User):
    total_mderators = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mderators += 1

    @classmethod
    def display_active_moderators(cls):
        return f"There are currently {cls.total_mderators} active Moderator"

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"

print(User.display_active_users())
u1 = User("Tom", "Garcia", 35)

print(User.display_active_users())
jasmine = Moderator("Jasmine", "O'conner", 61, "Piano")        
print(User.display_active_users())

jasmine_2 = Moderator("Meghan", "O'conner", 41, "Piano")        
print(User.display_active_users())
print(Moderator.display_active_moderators())

print(jasmine.full_name())
print(jasmine.community)


# python py_ch5_3_3_inhrt_eg.py




# Example 1: Roleplaying Game Classes
    # First define the Character class:

class Character():
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    # And then define the NPC class which inherits from Character.  It also calls the Character __init__() method using super().
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return "{0} says: 'I heard monsters running around last night!'".format(self.name)


