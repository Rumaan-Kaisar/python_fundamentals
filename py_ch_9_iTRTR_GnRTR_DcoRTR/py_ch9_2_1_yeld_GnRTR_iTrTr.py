
# Courses: colt_py_bootcamps    270

# -------------------------    Generators    -------------------------

# Generators are iterators
    # Subset of iterators: Every "GENERATOR" is "ITERATOR", but every "ITERATOR" is not a "GENERATOR"
    # Generators are easy and short way of creating iterators

# Generators are iterators, a kind of iterable you can 'only iterate over once'. 
    # Generators do not store all the values in memory, they generate the values on the fly



# Generators can be created in two ways:

    # Generators can be created with "GENERATOR FUNCTIONS" 
        # Generator functions use the "yield" keyword 

    # Generators can be created with "GENERATOR EXPRESSIONS"




# -------------------------    GENERATOR FUNCTIONS    -------------------------
    # it uses "yield"
    # can "yield" multiple times
    # it returns "GENERATOR"
    #  GENERATOR FUNCTIONS is a way to create a "GENERATOR" which is an "ITERATOR"



""" 
    --------------    Functions vs Generator Functions    --------------

    Functions:
        uses 'return'
        returns 'once'
        When invoked, returns the return 'value'

    Generator Functions:
        uses 'yield'
        can yield 'multiple times'
        When invoked, returns a 'generator'
"""




# ---------------    yield    ---------------------
""" 
    Syntax of the Yield Keyword in Python

    def gen_func(x):
        for i in range(x):
            yield i

What does the Yield Keyword do?
    yield keyword is used to create a generator function. 
    A type of function that is "memory efficient" and can be used like an "iterator object".

    In layman terms, the yield keyword will turn any expression that is given with it into a 
    generator object and return it to the caller. 
    Therefore, you must "iterate over" the "generator object" if you wish to obtain the values stored there. 
    we will see the yield python example. 
"""




# Example 1 (walkthrough): Our First Generator. (Actually we can call it a Generator-Generator)

def count_up_to(max): 
    count = 1
    while count <= max: 
        yield count 
        count += 1

# heres what happens: 
    # when "yield" executes it'll return the value as a "Generator" and pauses
    # it will stays pause untill "next()" is called upon "count_up_to" which acts on the returned "Generator"
        # then the execution resumes and "count" is incremented
        # the loop continues untill the while-condition is false
    
    # so "count_up_to "become an iterator it's similar to our previous custom iterator "cunter(low, high)" 
        # the difference is we are using only high/max values in ths case
        # we don't have to define next() or "StopIteration ERR" for generators, they're autometically defined

    # therefore creating iterator using generator is more easy.


# following retuns a Generator-Object
count_up_to(5)
<generator object count_up_to at 0x0000026CE31E1EE0>

# we can access the values as:
cnt = count_up_to(5)
next(cnt)   # returns values untill StopIteration ERR appear

# its memorizing its previous step, not all steps but immediate (recent one)
    # it storing one value at a time, 
    # so its more memory efficient, EG: "list" takes more memory than generators
    

# remember, we can only iterate once. Notice following execution
>>> cnt_2 = count_up_to(10)
>>> next(cnt_2)
1
>>> next(cnt_2)
2
>>> next(cnt_2)
3
>>> for num in cnt_2:
...     print(num)
...
4
5
6
7
8
9
10

# the for-loop autometically calls next() and handles "StopIteration" ERR




# Example 2: Week Generator.
            # Define the generator function "week"  which has a list of days.  
                # Iterate over the days and yield each day.   
                # After "Sunday", the generator is exhausted.  It does not start over.

def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day

>>> week = week()
>>> for day in week:
...     print(day)




# Example 3: Yes Or No Generator
            # yes_or_no  loops forever (while True) and yields answer , 
            # and then "toggles" answer from yes to no, or vice versa.
                # notice the new if-else style in an assignment statement

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if (answer == "yes") else "yes"


>>> toggler = yes_or_no()
>>> next(toggler)
'yes'
>>> next(toggler)
'no'
>>> next(toggler)
'yes'
>>> next(toggler)
'no'
>>> for state in toggler:
...     print(state)
...
yes
no
yes
no
yes
no
yes
no
yes
no
yes
no
yes
no
yes
no
yes
no
.
.
.


