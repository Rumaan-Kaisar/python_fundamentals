
# Courses: colt_py_bootcamps 279, 280


# ----------------    Higher-order-functions    ----------------
# We can pass funcs as args to other funcs



# Example 1: Following demonstrate higher order functiondef sum(nf func): total 0

# following function just adds applying whatever func
def sum(n, func):
    total = 0
    for num in range(n): 
        print(func(num))
        total += func(num)
    return total

# following function just squares the numbers
def square(x):
    return x*x

# following function cubes the numbers
def cube(x):
    return x*x*x

# passing the function "square()" as an argument of "sum()"
print(sum(10, square))

# passing "cube()" as an argument of "sum()"
print(sum(10, cube))

# 4:00




# ----------------    Nesting Functions    ----------------

# Example 2: We can use nested functions as follows
import random

# We can nest functions inside one another 
def greet(person): 
    def get_mood():
        msg = random.choice(('Hello there ', 'Go away ', 'I love you '))
        return msg

    result = get_mood() + person
    return result


print(greet("Toby") )


# note that we aren't actually returning a function, we just returning a value




# ----------------    Higher-order-function    ----------------
# Example 3: Following actually returns a function
import random

# We can nest functions inside one another 
def make_laugh_func(): 
    def get_laugh():
        lhg = random.choice(('HAHAHAH ', 'lol ', 'tehehe '))
        return lhg

    return get_laugh

# notice that "make_laugh_func" returns the function "get_laugh"

# for this reason following "laugh" is actually a function, not a variable
laugh = make_laugh_func()

# we have to call "laugh" with "()" to get the result
print(laugh())




# Example 4: Following is another example of nested-function, in this case we're using argumnets
import random

# We can nest functions inside one another 
def make_laugh_at_func(person): 
    def get_laugh():
        lhg = random.choice(('HAHAHAH ', 'lol ', 'tehehe '))
        return f"{lhg} {person}"

    return get_laugh

# notice that "make_laugh_func" returns the function "get_laugh"

# for this reason following "laugh" is actually a function, not a variable
laugh_at = make_laugh_at_func("Sam")

# we have to call "laugh" with "()" to get the result
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())



# NOTE: above is a way of creating higher-order-function




# ----------------    Decorators    ----------------
# we've already used "decorators" to define "class-methods" and "class-property"
# it is similar to Nested-functions just discussed above.
# it's just a function

# What's a Decorator??
    # Decorators are functions
    # Decorators wrap other functions and enhance their (functions that are being wrapped) behavior 
    # Decorators are examples of higher order functions 
    # Decorators have their own syntax, using @ (syntactic sugar)
     # We don't have to use it but we should!!
    

# Example 5: enhancing the behaviour of the "wrapped" function 

# without "@"
def be_polite(fn): 
    def wrapper():
        print("What a pleasure to meet you!") 
        fn()
        print("Have a great day!") 
        
    return wrapper

def greet():
    print("My name is Charlie Brown.")


#   note that, there is no relatioin between "be_polite" and "greet" yet
#	we are decorating our function
#	with politeness! 
greet = be_polite(greet) 
# notice, we used "greet" for our variable, we can use other names too
    # for example "greet_1",
    # we've used "greet" to name the varibale, because using-"@" will autometicaly do this
greet()


# wrapping another function
def bad_greet() :
	print("I hate You !!!")

# Notice that in this case we didn't use the "function-name" as "variable-name"
	# however "@" will use the same name
really_bad_greet = be_polite(bad_greet)
really_bad_greet()




# Decorator syntax: Using Syntactic sugar "@"

# Example 6: following does the same thing as above but here we've used "Decotor SyntaX"
def be_polite(fn): 
    def wrapper():
        print("What a pleasure to meet you!") 
        fn()
        print("Have a great day!") 
        
    return wrapper


@be_polite    
def greet():
    print("My name is Charlie Brown.")

@be_polite
def bad_greet() :
	print("I hate You !!!")


# We don't have to define the following lines anymore
# greet = be_polite(greet) 
# really_bad_greet = be_polite(bad_greet)

greet()
bad_greet()


# NOTE:
    # In the above example, the function "be_polite" is called "Decorator"
        # and the functions "greet" and "bad_greet" are DECORATED by "be_polite"
        # we don't have to name the function "wrapper", we can name it anything.

    # Also note that: '@be_polite' autometically connects "greet" and "bad_greet" with "be_polite"

    # But: In previous case, before applying "greet = be_polite(greet)" theer is no relation between "greet" and "be_polite"
        # so if we want to keep "greet" and "be_polite" seperate,
            # dont use "greet" as variable name
            # dont use "@-Decorator Syntax"




# python py_ch9_3_1_DcRTR_HyrOdrFunc.py

