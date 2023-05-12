
# Courses: colt_py_bootcamps    196

# -----------------    reversed() vs reverse()   -----------------
# (similar to sort() vs sorted())
# Returns a reversed iterator, 
# unlike reverse(), reversed() does not changes the oroginal obeject


# reverse() changes the original object
nuns = [1,2,3,4] 
nuns.reverse() 
# nuns
print(nuns) # [4, 3, 2, 1]


# reversed() does not changes
nuns_2 = [1,2,3,4] 
num = reversed(nuns_2) 
# reversed(nuns_2) 
# <list_reverseiterator object at 0x000001FAF02B7670>

# list(num)
print(list(num)) # [4, 3, 2, 1]
print(nuns_2) # [1, 2, 3, 4]

# Using with string
list(reversed("hello"))     # ['o', 'l', 'l', 'e', 'h']

# another example
for char in reversed("hello world"): 
    print(char)




# Example 1: Same thing can be done with LIST-SLICING, reversing with -1
"hello"[::-1]
# We have to work more to get same using reversed()
''.join(list(reversed("hello")))
# list(reversed("hello"))   # ['o', 'l', 'l', 'e', 'h']




# Example 2: Reverse FOR loop, counts backward
for x in reversed(range(0,10)):
    print(x)

    
