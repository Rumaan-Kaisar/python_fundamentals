
# Courses: colt_py_bootcamps 60 61 62 65
            # Topics : Boolian and Conbditional Logic
                # User input in Python
                # Trutiness
                # Usage of comparison operators


# -------------    User input in Python    -------------
''' General form:
                var = input("msg") 
'''

# the input data will stored in the variable "name"
name = input("Enter your name : ")
print("Hi there "+name) 

# Grab binput from different line
print("Enter your name :")
name = input()
print("Hi there "+name) 


# -------------    Conditional statements    -------------
# if-elif
'''
                if condition:
                    statements
                elif condition:
                    statements
                else:
                    statements     
'''



# Folowing operators are used to build LOOPing condition
# -------------    Comparison Operators    ------------- 
'''    
        Comparison operators are used to compare two values:

        Operator	    Name	                        Example	

        ==	            Equal	                        x == y	
        !=	            Not equal	                    x != y	
        >	            Greater than	                x > y	
        <	            Less than	                    x < y	
        >=	            Greater than or equal to	    x >= y	
        <=	            Less than or equal to	        x <= y
 '''



# -------------    Logical Operators    ------------- 
''' 
        Logical operators are used to combine conditional statements:

        Operator	    Description	                                                        Example

        and 	        Returns True if both statements are true	                        x < 5 and  x < 10	
        or	            Returns True if one of the statements is true	                    x < 5 or x < 4	
        not	            Reverse the result, returns False if the result is true	            not(x < 5 and x < 10)	
 '''



# -------------    Following used to control LOOPs    -------------

# -------------    Identity Operators    -------------
''' 
        Identity operators are used to compare the objects, 
        not if they are equal, but if they are actually the same object, with the same memory location:

        Operator	Description	                                                    Example

        is 	        Returns True if both variables are the same object	            x is y	
        is not	    Returns True if both variables are not the same object	        x is not y	
 '''



# -------------    Membership Operators : Frequently used with countables (Obj, List, Dict, Tuple etc)   -------------
''' 
        Membership operators are used to test if a sequence is presented in an object:

        Operator	Description	                                                                                Example

        in 	        Returns True if a sequence with the specified value is present in the object	            x in y	
        not in	    Returns True if a sequence with the specified value is not present in the object	        x not in y
 '''



# Use comparison in conditional statement
if name == "x" :
    print("Stop")
elif name == "o":
    print("done")
else:
    print("Crazy Frog")

# Indenting is important: following give indentation err
if name == "x" :
    print("Nothing happens")



# -------------    pass Statement    -------------
''' 
    ":" in if-elif expects indented-statement-blocks
        so if statements cannot be empty, but if you for some reason have an if statement with no content, 
        put in the pass statement to avoid getting an error. 
'''

if name == "x" :
    pass
print("Nothing happens")





# -------------    ELIF ladder    -------------
color = input("What's your favorite color?")
if color == 'purple':
	print("excellent choice!")
elif color == 'teal':
    print("not bad!")
elif color == 'seafoam':
    print("mediocre")
elif color == 'pure darkness':
    print("I like how you think")
else: 
	print("YOU MONSTER!") 

