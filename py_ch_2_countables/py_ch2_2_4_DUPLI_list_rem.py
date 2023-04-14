

# --------------     Duplication removal from a list    --------------
""" Method 1 - Naive Method 
    To remove duplicates from a list in Python, iterate through the elements of the list and 
    store the first occurrence of an element in a temporary list while ignoring any other occurrences of that element. """

# removing duplicates from the list using naive methods 

# initializing list 
sam_list = [11, 13, 15, 16, 13, 15, 16, 11] 

print ("The list is: " + str(sam_list)) 

# remove duplicates from list
result = [] 

for i in sam_list: 
    if i not in result: 
        result.append(i) 

# printing list after removal 
print ("The list after removing duplicates : " + str(result))


# Output: 
#  The list is: [11, 13, 15, 16, 13, 15, 16, 11]

#  The list after removing duplicates: [11, 13, 15, 16]




""" Method 2 - Using List Comprehension
Instead of using the For-loop to implement the Naive method of removing duplicates from a list, we can use Python's List comprehension functionality to do so in just one line of code. """

# removing duplicates from the list using list comprehension 

# initializing list 
sam_list = [11, 13, 15, 16, 13, 15, 16, 11] 

print ("The list is: " + str(sam_list)) 

# to remove duplicates from list 
result = [] 

[result.append(x) for x in sam_list if x not in result] 

# printing list after removal 
print ("The list after removing duplicates: " + str(result))

Output:
The list is: [11, 13, 15, 16, 13, 15, 16, 11]

The list after removing duplicates: [11, 13, 15, 16]



# ------------      dict.fromkeys()      Eliminate duplication --------------
# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

myLinklist = list(dict.fromkeys(liNks))

link_str = ""
for i in range(0, len(myLinklist)):
    link_str += (myLinklist[i]+"\n")

print(link_str)

"""
with open(file= "py_refined_links.txt", mode= "a+") as link_file:
    link_file.write(link_str)
"""
