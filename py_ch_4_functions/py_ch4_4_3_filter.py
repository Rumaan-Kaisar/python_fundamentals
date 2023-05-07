
# Courses: colt_py_bootcamps    188

# --------------    filter    --------------
# filter() used it with "lambdas"
    # The lambdas here, returns Boolians
# There is a lambda for each value in the iterable.
# filter() returns filter object, which can be converted into other iterables
    # it also ITRABLE ONCE
# The object contains only the values that return TRUE to the LAMBDA

list_1 = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, list_1))
evens # [2,4]

evns = filter(lambda x: x % 2 == 0, list_1)
list(evns)  # [2, 4]
list(evns)  # []: ITRABLE ONCE




# Example 1: Following filter the names starting with "A"
people = ["Darcy", "Christina", "Dana", "Annabel", "Alice"]
peeps_A = list(filter(lambda name: name[0]=='A', people) )
print(peeps_A)  # ['Annabel', 'Alice']



# Example 2: Filter the users that are not active
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

#extract inactive users using filter:
inactv = list(filter(lambda user: not user["tweets"], users))
# inactive_users = list(filter(lambda u: not u['tweets'], users))

# By checking length
inactive_users = list(filter(lambda u: len(u['tweets'])==0, users))
print(inactive_users)

#extract inactive users using LIST COMPREHENSION:
inactive_users2= [user for user in users if not user["tweets"]]




# --------------    combining MAP & FILTER    --------------
# extract usernames of inactive users using MAP and FILTER:
usernames = list(map(lambda user: user["username"].upper(), filter(lambda u: not u['tweets'], users)))
# ['JEFF', 'BOB123', 'GUITAR_GAL']

# extract usernames of inactive users w/ LIST COMPREHENSION
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
# ['JEFF', 'BOB123', 'GUITAR_GAL']




# Example 3:  Given this list of names:
names = ['Lassie', 'Saam', 'Rusty', 'Ploa']
# Return a new list with the string "Your instructor is " + each value in the array, but only if the value is less than 5 characters
list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) < 5, names)))
# ['Your instructor is Saam', 'Your instructor is Ploa']




# Example 4: Removing Negatives 
    # I define remove_negatives, which accepts a list I call nums
    # Then I call filter, passing the nums list and a lambda which returns True if an item is greater or equal to 0.
    # This filters out all the values that are negative
    # However filter doesn't return a list, so I have to cast it into a list and then return it
def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))

nums_1 = [1, 2, -3, 4, -5, -6, 0]
print(remove_negatives(nums_1))    # [1, 2, 4, 0]