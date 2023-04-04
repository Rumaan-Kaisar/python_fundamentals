
# Courses: colt_py_bootcamps    109, 110

# ------------|    Slice    |------------
# make new lists using slices of the old list
#       some_list[satart:end:step]
# similar to range(start, stop, step)

# use : afterward
    # what index to start slicing form
first_list = [1, 2, 3, 4]
first_list[1:]  # [2, 3, 4]
first_list[3:]  # [4], 4-th item
first_list[6:]  # [], no item found

# -ve numbers: slice that many back from the end
first_list[-1:]     # [4]
first_list[-3:]     # [2, 3, 4]



# only use : , gives the entire list
colrs = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colrs[2]
colrs[2:]
colrs[0:]   # gives copy of the list
# remember that, it is a copy of the list, not the original
colrs_2 = colrs[0:]     # make a copy of the list
colrs == colrs_2    # True,     indeed they have same values
colrs is colrs_2    # False,    they are not the same
# we can just use : to copy the list
colrs_3 = colrs[:]     # make a copy of the list
colrs_3 is colrs_2     # False,    they are not the same

colrs[-2:]     # ['indigo', 'violet']



# list[start : end]
# The end-index to copy up to (exclusive counting). "end index" is excluded
first_list = [1, 2,	3, 4]

# no start point, set 0 as start
first_list[ :2 ] # [1, 2]

first_list[:4] # [1, 2, 3, 4]
first_list[:len(first_list)]    # [1, 2, 3, 4]

# with start and end
first_list[1:3] # [2 , 3]

# -ve: With -ve numbers, 
    # how many items to exclude from the end (i.e. indexing by counting backwards)
first_list[:-1]     # [1, 2, 3]
first_list[:-2]     # [1 , 2]
first_list[1:-2]    # [2]
first_list[-4:-2]   # both negative, counted from back, [1, 2]



# list[start : end : step]
    # for example, a step of 2 counts every other number (1, 3, 5)
first_list = [1, 2, 3, 4, 5, 6] 
first_list[1::2]    # start from 2nd element and with 2 step [2, 4, 6] 
first_list[::2]     # start from ist element and with 2 step [1, 3]

# -ve step can be used for REVERSING
    # -ve steps, starts from backward
    # with -ve step, "end" is on the left of [1, 2, 3, 4, 5, 6]
first_list[::-1]     # [6, 5, 4, 3, 2, 1]
first_list[:3:-1]    # [6, 5]
first_list[:1:-2]    # [6, 4]
first_list[2::-1]    # [3, 2, 1]



# Tricks with slices

    # Reversing lists / strings
str_1 = "This os sucks"
str_1[::-1]     # reverses the string

    # Modifying portions of lists
seceond_list = [1, 2, 3, 4, 5, 6]
seceond_list[1:4:2] = ['a', 'b']
print(seceond_list)     # [1, 'a', 3, 'b', 5, 6]


colrs_2 = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colrs_2[::2]
colrs_2[::-1]
colrs_2[5][::-1]

# following reverses the strings 'red', 'yellow', 'blue', 'violet'
for clr in colrs_2[::2] :
    # clr[::-1] , reversing each string
    # index: returns the index of the passed item
    colrs_2[colrs_2.index(clr)] = clr[::-1]
print(colrs_2)     # ['der', 'orange', 'wolley', 'green', 'eulb', 'indigo', 'teloiv']

# index: returns the index of the passed item
colrs_2[colrs_2.index(clr)] = clr[::-1]

"helllllooo"[0]
"helllllooo"[:4]
"helllllooo"[::2]




# ------------|    Swapping values    |------------
names = ["James", "Michelle"] 
names[0], names[1] = names[1], names[0]   # swaps the values
print(names) # ['Michelle', 'James']

# Swaping is important for 
    # shuffling
    # sorting a list
    # data sructure algorithms
