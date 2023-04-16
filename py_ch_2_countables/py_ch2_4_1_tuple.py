
# Courses: colt_py_bootcamps    139,  140

# objectives:
    # create & access
    # builty-in methods: to modify & access
    # iterate: loops & comprehension
    # compare with lists & dictionaries    

# Tuple: items collection, Ordered, used inside ()
# It is 'IMMUTABLE': cannot be changed

# To create tuple:
    # Use () or  tuple(()) method 'double-round braces'
    # accessing is similar to "list"
    # there is also orders, like list


x = (1, 2, 3, 4) 
3 in x  # True
x[2]    # 3
x[2] = 0    # Type ERR, cannot be changed/update
x[-1]   # last item 4
# TypeError: 'tuple' object does not support item assignment



# other tuple 
list_1 = [1, 3, 5]
list_2 = [2, 4, 6]
# note the double round-brackets
tuple_two = tuple(( 'alpha', 'beta', 'gamma', 'lamda', list_1, list_2, 1, 2, 3))

tuple_two[-4][2]    # 6

# why tuples?
    # Faster than lists
    # Static data: makes a safer code
    # can be used as valid kays in dictionaries
    # some methods  returns tuples. EG: .items()


# Tuples can be used as valid kays in dictionaries
loactions = {
    (112, 345): "Kosko",
    (2323, 89): "Rabanna",
    (34, 67): "Tomillo"
}
loactions[(34, 67)]

# cannot use list as a key in a dictionary
loactions[[12, 34]] = "Bobo"    # ERR, TypeError: unhashable type: 'list'

# using tuple as a key
loactions[(12, 34)] = "Bobo"    # ok

loactions
# {(112, 345): 'Kosko', (2323, 89): 'Rabanna', (34, 67): 'Tomillo', (12, 34): 'Bobo'}


# some methods  returns tuples. EG: .items()
dummy_dict = {k : k**2 for k in range(0, 9)}
dummy_dict.items()  # returns a tuple
# dict_items([(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64)])
# Because we not going to update the returned values from .items(), we're going to use them with other things
    # to update the dictionary values we use the Dictionary methods




# -------------|    Tuple LOOPING and METHODS    |-------------
# Same as list
names_tup = ("jojo", "rabbit", "niley", "rupart")

for nam in names_tup:
    print(nam)

# using while loop, printing backward
i= len(names_tup) -1
while(i >= 0):
    print(names_tup[i])
    i -= 1


# Tuple methods: There are two tuple methods

# count: number of times the value appear in a tuple
x = (1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3)
x.count(3)  # 6
x.count(1)  # 3

# index: returns the first matching index of a found value
x.index(3)  # 2
x.index(5)  # 4
x.index(8)  # value ERR



# -------------|    NESTED TUPLE: Same as NESTED-LIST    |-------------
nest_tup = (1, 2, 3, 4, 5, 6, 7, (1, 1, 2, 2), 2, (3, 3, 3), 3, 3)
nest_tup.index((1, 1, 2, 2))
[print(i) for i in nest_tup[7]]
list_tup_nm = [i for i in nest_tup[7] if i]


# Slicing is similar to list, non inclusive last 
nest_tup[3:]    # (4, 5, 6, 7, (1, 1, 2, 2), 2, (3, 3, 3), 3, 3)
nest_tup[0:4]    # (1, 2, 3, 4)
nest_tup[3::2]  # using steps:  (4, 6, (1, 1, 2, 2), (3, 3, 3), 3)

    
