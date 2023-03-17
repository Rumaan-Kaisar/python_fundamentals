# Courses: colt_py_bootcamps    81, 83
''' 
    ----------|    for loops    |----------
    In Python, for loops are written like this:
        
        for item in iterable_object:
            # do something with item

    iterable: An iterable object is some kind of 'collection of items', for instance: 
        a list of numbers, 
        a string of characters, 
        a range, etc.

    item: item is a new variable that can be called whatever you want: any identifier
        item references the current position of our iterator within the iterable. 
        It will iterate over (run through) every item of the collection and then go away when it has visited all items
'''

# Following demonstrates for loop with three iterable types

# ----------|    for loop with RANGE    |----------
    # Excluded the last number

for i in range(1, 10):
    print(i)    # prints 1 to 9



# ----------|    for loop with String    |----------
    # Through all elements
for ch in "coffee":
    print(ch)    # prints all seperate letters



# ----------|    for loop with List    |----------
    # Through all elements
for i in [23, 67, 89]:
    print(i)

