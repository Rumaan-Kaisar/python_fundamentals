# Courses: colt_py_bootcamps    141,  142, 143

# objectives:
    # create & access
    # builty-in methods: to modify & access
    # iterate: loops & comprehension
    # compare with lists & dictionaries    

# sets: formal MATHEMATICAL SETS, something like combination of DICT and LIST
    # No DUPLICATE values
    # No order
    # CANNOT accessed by INDEX
    # useful; keep track but dont care order, and NO DUPLICATE



# To create tuple:
    # Use {} or  set({})
# No DUPLICATES
set1 = set({1, 1, 2, 3, 3, 3, 4})   # {1, 2, 3, 4}

# Creating a new set
set2 = set({1 , 2, 3})  # usding set() method
set3 = {1 , 2, 3}  # usding {}

# existance of element
4 in set3   # False
2 in set3   # True



# ------------    Accessing    ------------
# do not support indexing
set2[1] # ERR

# Use for loop
nums = {1, 2, 3, 3, 4, 5, 6, 7}
for n in nums:
    print(n)

# common usage of sets
# Eliminating DUPLICATE items
num_list = [1, 1, 2, 3, 3, 3, 4]
set(num_list)   # eliminate all DUPLICATIONS: {1, 2, 3, 4}
print(list(set(num_list)))  # convert back to list: [1, 2, 3, 4]
len(num_list)




# ------------    Set methods    ------------
# add(): adds element
s = set([1, 2, 3])
s.add(4)
s
# if an element already exits, no ERR occurs
s.add(5)
s.add(5)
s

# remove(): removes item from a set
s.remove(2)
s # {1, 3, 4, 5}
# ERR if the item is not present
s.remove(7)  # ERR

# discard(): To avoid key ERR, use .discard()
s.discard(7)  # no ERR
s
s.discard(1)  # also removes the found item
s # {3, 4, 5}

# copy(): creates copy of a existing set (not point to same obj)
so = set([1, 2, 3])
copy_so = so.copy()
copy_so
copy_so is so   #  False

# clear(): removes all the contents
copy_so.clear()
copy_so




# ------------    Set MATH    ------------
# subset of math in real world
# mathematical methods like:
    # intersection
    # symmetric difference
    # union

# union (returns unique elements): use | as OR
set_01 = {1, 2, 3, "a", "v", "c"}
set_02 = {8, 2, 3, "a", "n", "l"}
set_01 | set_02     # {1, 2, 3, 'v', 8, 'n', 'c', 'l', 'a'}

# intersection (coomon in both sets): & as AND
set_01 & set_02     # {2, 3, 'a'}



# coolect Uniques - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called "unique_stuff" which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)



