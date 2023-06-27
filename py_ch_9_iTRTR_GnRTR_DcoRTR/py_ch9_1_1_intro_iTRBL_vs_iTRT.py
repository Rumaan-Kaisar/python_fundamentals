
# Courses: colt_py_bootcamps    265, 266

# Objectives: 
    # part 1: ITEARTORS
        # Difference between ITERATOR and ITERABLE
            # Define Iterator and Iterable 

        # User defined ITERATOR
            # Understand the iter() and next() methods

        # How make our CLASS ITERABLE

        # Detail on how loops work
            # Build our own for loop


    # part 2: GENERATORS
        # Define what generators are and how they can be used 
            # How GENERATORS are related to iterators

        # Compare 'generator FUNCTIONS' and 'generator EXPRESSION's 
        # Use generators to PAUSE execution of expensive functions




# --------------    iterator vs iterable    --------------

# these are related to loops and iteratings


# Iterator
    # iterator: iterated upon. next() returns the next element
        # An object that can be iterated upon. 
        # An object which 'returns data', one element at a time when next() is called on it.


# Iterable
    # iterable: object on which iter() is called. next() doesn't work
        # An object which will return an Iterator when iter() is called on it.




# Example 1: 
    # Iterable: "HELLO" is an 'iterable', but it is not an 'iterator'.
        # any "list" & "string" are ITERABLES

    # Iterator: iter("HELLO") returns an iterator. 





# ----------------    How FOR-LOOP works    ----------------:
# FOR-LOOP doesn't act directly upon a "list" or "string"
# it applies iter() first and then call next() untill End is arrived - i.e "StopIteration ERR" occurs




# Example 2: following also demonstrate iterator vs iterable
nam = "richard"

# 'nam' is not an iterator, because we can't apply next() upon it
next(nam)   # ERR: 'str' object is not an iterator

# however, applying iter() upon 'nam' will return an iterator
itr = iter(nam)     # returns an iterator: <str_iterator object>

next(itr)   # r
next(itr)   # i
next(itr)   # c
next(itr)   # h





# -------------    <list_iterator object>  and  <str_iterator object>    -------------
    # <list_iterator object>: iter()  applied on a list
    # <str_iterator object>: iter()  applied on a string

mun = [1,2,3,4]

mun_itr = iter(mun)     # <list_iterator object at 0x0000019FCACC7DC0>





# -------------    next()    -------------
    # When next() is called on an iterator, the iterator returns the next item. 
    # It keeps doing so until it raises a "StopIteration ERROR".

>>> next(itr)   # 'a'
>>> next(itr)   # 'r'
>>> next(itr)   # 'd'
>>> next(itr)   # StopIteration



