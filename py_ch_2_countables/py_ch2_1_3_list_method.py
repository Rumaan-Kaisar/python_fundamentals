
# Courses: colt_py_bootcamps    104, 106, 107

# There are bunch of list methods
ls_ex_1 = [1, 2, 3, 4, 5]

# length: len()
print(len(ls_ex_1))




# ----------|    Adding data to a list    |----------

# Append: adds single data
ls_ex_1.append(6)
print(ls_ex_1)

# extend: adds multiple data. add to list the multple values are passed
ls_ex_1.extend([7, 8, 9])
print(ls_ex_1)

# insert : insert an item to a given position, need to specify an index
ls_ex_1.insert(2, "three")  # insert "three" at the index 2
print(ls_ex_1)  # 1, 2, "three", 3, . . .

ls_ex_1.insert(-1, "end")  # DIFFERENT: insert "end" at the 2nd to the last
print(ls_ex_1)  # 1, 2, "three", 3, . . ., "end", 4

ls_ex_1.insert(len(ls_ex_1), "WorldsEnd")   # To add something to the last
print(ls_ex_1)



# ----------|    Removing Data from a list    |----------
# clear:: Remove all the items from a list
ls_ex_2 = ['a', 'b', 'c', 6, 7, 7, 8]
print(ls_ex_2)
ls_ex_2.clear()
print(ls_ex_2)

# pop: Remove single element, specify the index. if no-index, removes the last item
ls_ex_2 = ['a', 'b', 'c', 6, 7, 7, 8]
poped_item = ls_ex_2.pop(-2)    # returns the poped item and stores it in a variable
print(ls_ex_2)
print(poped_item)
ls_ex_2.pop()   # returns the poped item
print(ls_ex_2)

# remove: removes the first matching item to the passed item (not an index), ERR if item not found
ls_ex_3 = ['a', 'b', 'c', 6, 7, 6, 8, 7, 8]
ls_ex_3.remove("b")
print(ls_ex_3)
ls_ex_3.remove(7)
print(ls_ex_3)


# ----------|    accessing    |----------
# index: returns the index of the passed item
print(ls_ex_3.index("c"))
# specify start and end: index(item, start, end), finds item between start and end
# print(ls_ex_3.index(7, 0, 3))   # finds 7 between 1st & 4th element, gives ERR
print(ls_ex_3.index(7, 4, 7))   # finds 7 between 5th & 8th element
print(ls_ex_3.index(7, 3))  # finds 7 after the 4th element
print(ls_ex_3.index(7, -3))  # finds 7 after the last-3rd element

# Count: retuns the number of occurance of the passed element in a list
print(ls_ex_3.count(7))

# reverse: reverse the elemnts of the list (in-place)
print(ls_ex_3)
print(ls_ex_3.reverse())
print(ls_ex_3)

# sort: sort the elemnts of the list (in-place)
ls_ex_4 = ["nba", "banana", "mangola", "Zoho"]
print(ls_ex_4)
print(ls_ex_4.sort())   # alphabetically
print(ls_ex_4)

# join: Is a STRING mentod, "converts a list to string". 
# base_str.join(itr): concatenate a copy of base-str (space or other char) between each item of the iterable (list, tuple)
print('+'.join(ls_ex_4))
str_jnd = ' '.join(ls_ex_4)
print(f"the string is {str_jnd}, {type(str_jnd)}")
print(' Hellow '.join(ls_ex_4))




# ------------|    More Examples    |------------
# A solution using append()

# Create a list called instructors
instructors = []

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")



# A solution using extend()

# Create a list called instructors
instructors = []

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
    
# Use any of the list methods we've seen to accomplish this:
instructors.extend(["Colt", "Blue", "Lisa"])



# A "grosser" solution that still technically works.  (it's grosser because it requires you to know the exact positions you want to add data to)

# Create a list called instructors
instructors = []

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
    
# Use any of the list methods we've seen to accomplish this:
instructors[0] = "Colt"
instructors[1] = "Blue"
instructors[2] = "Lisa"


# python py_ch2_list_method.py
