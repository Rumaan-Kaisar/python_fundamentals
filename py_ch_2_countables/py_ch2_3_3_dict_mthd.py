
# Courses: colt_py_bootcamps    128,  131

# ----------|    Dictionary Methods    |----------
# clear()
d = dict(a=1, b=2, c=3)
d
d.clear()
d



# ----------|    copy()   |----------
d = dict(a=1, b=2, c=3)
c = d.copy()   # makes a clone
c
# but clone is not same
d is c # False, they're not stored at the same place



# ----------|    fromkeys()   |----------
# fromkeys(), creates key-value pairs from given comma seperated values
    # first argument is an iterable
    # use with {} or "dict"
{}.fromkeys("key", "vaal")  # string is considered as iterable object {'k': 'vaal', 'e': 'vaal', 'y': 'vaal'}
{}.fromkeys("k", "vaal")    # {'k': 'vaal'}
dict.fromkeys(["key"], "vaal")    # {'key': 'vaal'}

    # it is good for creating defaul values, following for example
{}.fromkeys( ["name", "owns_dog", "numcourses", "favorite_language", "is_hilarious", 44], "unknown")
{}.fromkeys(['name', 'email', 'profile_bio', 'score'], None)

{}.fromkeys("k", [1, 3, 5])    # {'k': [1, 3, 5]}
new_user = dict.fromkeys([])
new_user.fromkeys(range(0,11), None)
# {0: None, . . .  10: None}



# ----------|    get()   |----------
# retrive values from corresponding "key", None instead of key-error
d = dict(a=1, b=2, c=3)
d['a']          # 1
d.get('a')      # 1
d['b']          # 2
d.get('b')      # 2
d['No_key']     # KeyError
d.get('No_key') # None



# ----------|    pop()   |----------
# pop(), removes a specified key from a dictionary
d = dict(a=1, b=2, p=3)
d.pop() # TypeError: pop expected at least 1 arguments, got 0 
d.pop('a') # 1 
d # {'b': 2, 'p': 3}
d.pop('e') # KeyError

instructor = {
    "name": "Cbolt",
    "owns_dog": True,
    "numcourses": 4,
    "favorite_language": "Python", 
    "is_hilarious": False,
    44: "my favorite number !"
}

instructor.pop("numcourses")



# ----------|    popitem()   |----------
# popitem(), removes a ranom key in a dictionary
    # generally removes items from the last
d = dict(a=1,b=2, c=3,d=4,e=5) 
d.popitem() # ('e', 5)
d.popitem('a') # TypeError: popitem() takes no arguments (1 given)
instructor.popitem()



# ----------|    update()   |----------
# update() 
# updates key-value pair in a dictionary with another set from otehr key-value dictionary
first = dict(a=1, b=2, c=3, d=4, e=5) 
second = {}
second.update(first)
second # {'a': 1,	'b': 2,	'c': 3,	'd': 4,	'e': 5}

#	let's overwrite an existng key 
second['a'] = "AMAZING"     # {'a': 'AMAZING', 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# if we update again, the update overrides our values
second.update(first) # {'a': 1,	'b': 2, 'c's 3,	'd': 4, 'e's 5}
second  # {'a': 1,	'b': 2,	'c': 3,	'd': 4,	'e': 5}

# update() does not remove things, its oly additive
second.update({})
second  # {'a': 1,	'b': 2,	'c': 3,	'd': 4,	'e': 5}



# Example 1: Bakery Dictionary Exercise. The following code is common to all solutions:
# This code picks a random food item:
from random import choice       #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])         #DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# Solution using IN: test if a value is contained in a dictionary:
# Retrive value using in
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")
    
# Solution using get(): The variable will either contain the corresponding value from the dictionary OR None.  We can write a simple conditional check:
# Retrive value using get()
quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")
    

        
# Example 2: Fromkeys Exercise, creat a dictionary by intializing following keys
game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements"
]
initial_game_state = dict.fromkeys(game_properties, 0)    
