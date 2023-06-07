
# Courses: colt_py_bootcamps    240

# ------------    Instance Attributes and Methods    ------------

# All INSTANCE METHODS are defines after __init__()
    # to work with we need to add "self" as a parameter

class User:
    def __init__(self, first, last, age):
        self.first = first 
        self.last = last 
        self.age = age

    def full_name(self):
        return f"{self. first} {self. last}"

    def initials(self):
        return f"{self.first[0]}. {self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self): 
        self.age += 1
        return f"Happy {self.age}th, {self.first}"



user_1 = User("Joe", "Smith", 68) 
user_2 = User("Blanca", "Lopez", 41) 
print(user_2.full_name())    

print(user_1.likes("Ice Cream"))
print(user_2.likes("Chips"))
print(user_1.initials())
print(user_2.initials())

print(user_1.is_senior())
print(user_1.age)
print(user_1.birthday())
print(user_1.age)




# Example 1: Create a "Bank Account" class

class BankAccount:

    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

owner_1 = BankAccount("Mr. Anderson")        
print(owner_1.getBalance())
owner_1.deposit(700)
print(owner_1.getBalance())
owner_1.withdraw(120)
print(owner_1.getBalance())


# python py_ch5_1_4_atrbMethd.py

