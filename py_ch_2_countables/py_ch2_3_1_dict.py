
# Courses: colt_py_bootcamps    121, 123, 125

# objectives:
    # Describe, create and access DICTIONARY
    # modify & copy using built-in methods
    # iterate: loops & Comprehensions
    # Dictionary vs List




# -------------|    Ditionary    |-------------
# limitation of list: Cannot orhanize data.
# Ditionary: key-value pair data structure. Better than list to organize the data.
# There is no order like "lists"

player = {
    "name": "Nymer",
    "owns_dog": True,
    "num_trophies": 20,
    "favorite_player": "Pele",
    "high_sense_of_humer": True,
    44: "favorite_number"
}


# Use "dict" to construct a dictionary
# assign values to key by specifying: key = 'value'
another_dict = dict(name = 'Salazar', age = '2000')  # key doesnt have to be quoted
print(another_dict)



# -------------|    Accessing a Ditionary    |-------------

player['name']

# List of dictionaries
cart = [{"item_name": "mango", "price": 40}, 
        {"item_name": "banana", "price": 30}, 
        {"item_name": "orange", "price": 50}, 
        {"item_name": "strawberry", "price": 80},
        {44: "not an error"} ]

# accessing a dictinary from a list  of dictionaries
cart[2]["item_name"]    # 'orange'
cart[-1][44]    # 'not an error'


# -------------|    Accessing using loops: key(), value(), items()    |-------------
# use   .keys() and .values() methods
player.values()
player.keys()

for key in player.keys():
    print(f"{key} : {player[key]}")

# use .items()  to access both key-value
    # returns a list of "TUPLES", we access key-value using 0 , 1 index
player.items()  # dict_items([('name', 'Nymer'), . . . . , (44, 'favorite_number')])
for itm in player.items():
    print(f"{itm[0]} : {itm[1]}")

# or we can use PAIR of loop variables
for key, val in player.items():
    print(f"key is {key} : value is {val}")


    
