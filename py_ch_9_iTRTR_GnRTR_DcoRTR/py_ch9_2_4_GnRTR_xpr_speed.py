
# Courses: colt_py_bootcamps    278

# --------------    GENERATOR-Expression    --------------

    # You can also create GENERATORS from "GENERATOR EXPRESSIONS" 
    # Generator expressions look a lot like list comprehensions 
    # Generator expressions use () instead of []

    # It also returns "StopIteratiuon ERR" after end of the generator
    # It also eccessable only once


# using GENERATOR FUNCTION
def nums():
    for num in range(10): yield num

g = nums()
next(g)

# >>> next(g)
# 0
# >>> next(g)
# 1
# >>> next(g)
# 2
# >>> next(g)
# 3
# >>> next(g)
# 4
# >>> next(g)
# 5



# same result, using GENERATOR EXPRESSION
g_2 = (num for num in range(10))
next(g_2)

# >>> next(g_2)
# 0
# >>> next(g_2)
# 1
# >>> next(g_2)
# 2
# >>> next(g_2)
# 3
# >>> next(g_2)
# 4
# >>> next(g_2)
# 5


# Example 0: if we need to use a list only once we can use the "Generator expression" over "List"
sum(num for num in range(1,10))  # is beter than 
sum([num for num in range(1,10)]) 




# Example 1: Execution speed test of GENERATORS vs LIST
import time     # we use it to calculate time of execution


# =-=-=-=-=-=    WITHOUT A GENERATOR    =-=-=-=-=-=

# SUMMING 10,000,000 (10 million) Digits With List Comprehension 
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
# calculate the elapsed time
list_time = time.time() - list_start_time	# end time - start time


# =-=-=-=-=-=    USING A GENERATOR-Expression    =-=-=-=-=-=
# to create a GENERATOR-Expression we have to create a "LIST-COMPREHENSION-SIMILAR-thing" but using "()" instead of "[]" 

# SUMMING 10,000,000 Digits With Generator Expression
gen_start_time = time.time() # save start time
# notice the usage of () in the following comprehension which is a "GENERATOR-Expression"
print(sum(n for n in range(100000000)))
# calculate the elapsed time
gen_time = time.time() - gen_start_time     # end time - start time

print(f"sum(n for n in range(100000000)) took: {gen_time}")
print(f"sum([n for n in range(100000000)]) took: {list_time}")


# output:
	# ========    for 10 million    ========
	# sum(n for n in range(10000000)) took: 1.1561200618743896
	# sum([n for n in range(10000000)]) took: 1.0898852348327637


	# ========    for 100 million    ========
	# sum(n for n in range(100000000)) took: 12.79152226448059
	# sum([n for n in range(100000000)]) took: 13.308600664138794






# ----------------    GENERATOR-function and GENERATOR-Expression    ----------------
""" 
    GENERATOR-functions
        GENERATOR-functions are written just like a normal function but we use yield() instead of return() for returning a result. 
            Unlike regular functions which on encountering a return statement "terminates entirely", 
                generators use a "yield statement" in which the state of the function is saved from the last call and 
                can be picked up or resumed the next time we call a generator function.

        generator  takes much less memory. 
        _next_() and _iter_() make the generator function more compact and reliable.  
"""
    

# Example 2 : Following is a "GENERATOR-function" it illustrate generator, yield() and next().

def generator():
    t = 1
    print ('First result is ',t)
    yield t
 
    t += 1
    print ('Second result is ',t)
    yield t
 
    t += 1
    print('Third result is ',t)
    yield t


call = generator()
next(call)
next(call)
next(call)


# Output : 

    # First result is  1
    # Second result is  2
    # Third result is  3






# =================    Difference between Generator function and Normal function    =================

#     1. Once the function yields, the function is paused and the control is transferred to the caller.
#     2. When the function terminates, StopIteration is raised automatically on further calls.
#     3. Local variables and their states are remembered between successive calls.

#     4. The 'generator function' contains "ONE or MORE yield statements" instead of a "return statement".
#     5. As the methods like _next_() and _iter_() are implemented automatically, we can iterate through the items using next().




""" 
    GENERATOR-Expression
    GENERATOR-Expression is similar to "list comprehensions" but instead of "[]" brackets we use parenthesis "()". 
        These expressions are designed for situations where the generator is used right away by an enclosing function. 
        Generator expression allows creating a generator without a yield keyword. 
        However, GENERATOR-Expression "doesn’t share the WHOLE POWER" of the GENERATOR-function. Example :  
"""

# Example 3: Python code to illustrate GENERATOR-expression
generator = (num ** 2 for num in range(10))
for num in generator:
    print(num)

""" 
Output : 
    0
    1
    4
    9
    16
    25
    36
    49
    64
    81 
"""




# Example 4: We can also generate a LIST using GENERATOR EXPRESSIONS. 
#             just use list() to convert the gnerator-obj

string = 'pliha'
li = list(string[i] for i in range(len(string)-1, -1, -1))
print(li)       # ['a', 'h', 'i', 'l', 'p']

