
# Courses: colt_py_bootcamps    193, 194, 195

# -------------------    sorted    -------------------
# Can work with TUPLE or LIST or anything that is ITERABLE
    # returns new sorted list from the items in ITERABLE
    # doesnot change the original object

num1 = [1, 2, 5, -7, 0]
sort1 = sorted(num1)    # [-7, 0, 1, 2, 5]


# ----------    difference between "sort" and 'sorted'    -----------
# sort() changes the object but sorted() doesn't
# sort() works with LIST, sorted() works with other iterables

num2 = [1, 2, 5, -7, 0]
sorted(num2)    # doesn't changes the object
# [-7, 0, 1, 2, 5]
print(num2)
# [1, 2, 5, -7, 0]

num3 = [1, 2, 5, -7, 0]
num3.sort() # changes the object
print(num3)     # [-7, 0, 1, 2, 5]

# with tuple
num_tup = (5, -7, 0)
sorted(num_tup)    # returns list: [-7, 0, 5]




# Example 1: Working with dataset
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]


# sort according to length, large dictionaries appeats at the end
sorted(users, key = len)


# To sort users by their username, use LAMBDA
sorted(users,key=lambda user: user['username'])


# Finding our most active users...
# Sort users by number of tweets, descending; used reverse=True for descending order
sorted(users,key=lambda user: len(user["tweets"]), reverse=True)




# Example 2: Working with Song dataset
# ANOTHER EXAMPLE DATA SET==================================
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
sorted(songs, key=lambda s: s['playcount'])
# sorted(songs, key = lambda sng: sng['playcount'], reverse = True)







# -------------------    min & max    -------------------
# max/min: Return the largest/smallest item in an iterable or the largest/smallest of two or more arguments.
# max (strings,	dicts with	some keys)
# min (strings,	dicts with	some keys)
# can also works with list, dictionary or tuples 


max(3, 67, 99)  # 99
max('s', 'e', 't')  # 't'

max([3,4,1,2])	# list: 4	
max((1,2,3,4))	# tuple: 4	
max('awesome')	# string: 'w'	
max({1: 'a', 3 :'c', 2:'b'})	# dictionary: 3


nums = [40,32,6,5,10] 
max(nums)   # 40
min(nums)   # 5
max('hello world1?')    # 'w'
min("hello world")  # ' '




# Example 3: find the shortest name alphabetically and by length
names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# Default: it finds ALPHABETICALLY
min(names)  # 'Arya'

# finds the minimum length of a name in names
min(len(name) for name in names) # 3
min(names, key = lambda nm: len(nm)) #'Tim'

# find the longest name itself
max(names, key=lambda n:len(n)) #Ollivander




# Example 4: Find the max played song and its title
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]


# max played song
max(songs, key = lambda sn: sn['playcount'])    
# {'title': 'YMCA', 'playcount': 99}
# Get the title
max(songs, key = lambda sn: sn['playcount'])['title']

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA


# Same thing using for loop
maxiMum = 0
for sng in songs:
    if sng['playcount'] > maxiMum :
        maxiMum = sng['playcount']
print(maxiMum)  # 99




# Example 5: find the Extremes from some given numbers

    # I call min(nums) and max(nums)
    # I wrap the values I get back in a new tuple and return it!

def extremes(nums):
    return(min(nums), max(nums))

print(extremes((1, 2, 5, -7, 0)))   # (-7, 5)

