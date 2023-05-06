
# Courses: colt_py_bootcamps    186

# --------------    map    --------------
# its a "built in function", we can use it with "lambdas"

# map is a built in standard function that accepts at least two arguments, 
    # a function (usually a LAMBDA) 
    # an "iterable" - something that can be iterated over (lists, strings, dictionaries, sets, tuples)

# It runs the lambda for each value in the iterable and returns a "map object" which can be converted into another data structure

nums = [1, 2, 3, 4, 5]

doubles = map(lambda x: 2*x , nums)

# map object: Can be iterate only once
list(doubles)       # [2, 4, 6, 8, 10]
list(doubles)       # []: "map-objects" only iterated once

# following not gonna work: "map-objects" only iterated once, doubles is a map object
for num in doubles:
    print(num)

# one solution is, convert the "map object" to a list during its creation


# Example 1: Convert to uppercase using lambda and map
people = ["Darcy", "Christina", "Dana", "Annabel"]
peeps = map(lambda name: name.upper(), people) 
list(peeps)     # ['DARCY', 'CHRISTINA', 'DANA', 'ANNABEL']
print(list(peeps))  # []: "map-objects" only iterated once



# Example 2: Create a list of evens using lambda and map
liST_1 = [1, 2, 3, 4, 5]
evens = list(map(lambda x: x*2, liST_1))
print(evens) # [2,4,6,8,10]




# --------------    map & lambda with dictionary    --------------
# Example 3: Accessing from list of dictionary, using lambda & map
names = [
        {'first':'Rusty',	'last':	'Camlar'},
        {'first': 'Palmer', 'last':	'Spancer' },
        {'first': 'Blue', 'last':	'Steele', }
]

first_names = list(map(lambda x: x['first'], names))
print(first_names)




# Using functions instead of lambdas
# we can use any defined functions with a map

# Example 4: Use a function with a map
liST_1 = [1, 2, 3, 4]

def double(x): return x*2

doubles_list = map(double, liST_1)

print(list(doubles_list))   # [2, 4, 6, 8]
print(list(doubles_list))   # []: "map-objects" only iterated once




# Example 5: Create a list of decreemnetd nubers using map & lambda
    # define the function "decrement_list" that accepts a list called l
    # call map and pass in a lambda and the list

    # The lambda returns n-1 for each n in the list

    # The last step is to convert the return value of map to a list
    # Remember, map returns a <map object>, not a list

    # finally we return the result!

def decrement_list(l):
    return list(map(lambda n: n-1, l))

liST_1 = [1, 2, 3, 4]
print(decrement_list(liST_1))
print(decrement_list(liST_1))

# python py_ch4_4_2_map.py