
# Courses: colt_py_bootcamps    148, 150, 151 

# --------------|    OUTPUT from a function    |--------------
# Get OUTPUT: To return values from a function we need to use "return"
    # "return" will exit the function and 
        # no statement will execute inside the function taht appers after 'return'

    # "return" can return anything.
        # can return tuple, list, dictionary, string etc
        # tuple is used to retrunn multple values at a time

    # "return" pops the functiin from 'call-stack'


# Following doesn't work
def sqr_of_2():
    7**2

a = sqr_of_2()
print(a)


# We have to use 'return' key
def sqr_of_2():
    return 7**2
    print("Never executed")

b = sqr_of_2()
print(b)




# Example 1: simple function
def speak_pig():
    return 'oink'




# Example 2: write a function that generates EVEN numbers
    # Generating evens using a list comprehension:
def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]

    # Generating evens using a loop:
def generateEvens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result

