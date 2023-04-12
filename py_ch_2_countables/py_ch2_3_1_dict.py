
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


    
# Example 1: Create a dictionary called "user_info"  and add at least 3 key value pairs to it (totally up to you what they are)
# There is no single correct answer.  Here are 2 potential solutions:
user_info = {"name": "Blue", "age": 10, "email": "blue@gmail.com"} 
user_info = {"city": "Paris", "temperature": 59.0, "is_raining": True} 



# Example 2: concatenate strings from the given dictionary
artist = {
        "first": "Neil",
        "last": "Young",
}
    
# concat first and last name with a space
full_name = artist["first"] + " " + artist["last"]

# Solution using the format() method:
full_name = "{} {}".format(artist["first"], artist["last"])

# F-String Solution: pay attention to our quotes in this solution!
full_name = f"{artist['first']} {artist['last']}"



# Example 3: Loop over 'donations', add all the VALUES together and store in a variable called "total_donations"

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = 0
for donation in donations.values():
    total_donations += donation

# Advanced Version 1: This solution uses a built-in function called sum() covered in the "Lambdas and Built-In Functions" section.
total_donations = sum(dntn for dntn in donations.values())

# Advanced Version 2: An even better solution using the same sum() built-in function is just this nice little line:
sum(donations.values())


