# Courses: colt_py_bootcamps 54

# ----------  Formatting String   ----------
    # F-string is the best option
    # Python 3.6        F-string,       any math/opr canbe done inside the {}
"""     Float precision in the f-String method:

        Syntax: {value:{width}.{precision}} 
"""

# Float precision in the f-String 
num = 3.14159
print(f"The valueof pi is: {num:{1}.{3}}")

x = 10;
formatted_string = f"I've told you {x} times already"
print(formatted_string)

formatted_string += f" also concatenates {12/8} times"
print(formatted_string)

# Arithmetic operations using F-strings
a = 5
b = 10
print(f"He said his age is {2 * (a + b)}.")



# Other way: Python 2 -> 3.5:       str.format()        method [less readability]
    # Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

    # The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars.\n"
print(myorder.format(quantity, itemno, price))

    # Placing using index: You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
print("I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price))




# Another way:      %-formatting        [poor readability]
# String objects have a built-in operation using the % operator, which you can use to format strings.
name = "Eric"
str_x = "Hello, %s." % name
print(str_x)

# In order to insert more than one variable, you must use a tuple of those variables.
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print("Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (first_name, last_name, age, profession, affiliation))

# F-sreing is much better
print(f"Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}.")



""" 
There are four different ways to perform string formatting in Python:
    Formatting with % Operator.
    Formatting with format() string method.
    Formatting with string literals, called f-strings.
    Formatting with String Template Class 
"""

print("The mangy, scrawny stray dog %s gobbled down" + "the grain-free, organic dog food."%'hurriedly') # ERR occurs
print("The mangy, scrawny stray dog %s gobbled down the grain-free, organic dog food."%'hurriedly') # no concat

x = 'looked'
 
print("Misha %s and %s around"%('walked',x))

