
# Courses: colt_py_bootcamps    184

# --------------    Lambdas    --------------
# It is a function that has "NO NAME", also called "ANONYMOUS FUNCTION"
# used in a variable

# normal function: no lambda
def sqr(num): return num*num

print(sqr(3))

# Following is the lambda that does exact same thing
sqr_2 = lambda num: num*num
print(sqr_2(3))

# using multple parameter
add_ld = lambda a, b : a+b
print(add_ld(3, 7))


# Lambdas has no name
print(sqr.__name__) # named function
print(add_ld.__name__) # <lambda>
print(sqr_2.__name__) # <lambda>




# ------    Usage of lambda    ------
''' lambdas are used as small functions that needs to 
go inside another function as a parameter
these functions usually onlu used once or twice '''
# It also avoids IMMIDIATE EXECUTION, like named function with (), we just define the lambda
# notice the lambda inside Button(), 
    # we dont need to define another function to print "Hello"
button = tk.Button(frame, text "CLICK ME", fg = "red", command = lambda: print("Hello"))




# Example 1: TK- buttonimport tkinter as tk
# DON'T WORRY ABOUT ANY OF THIS CODE
root = tk.Tk()#=====================
frame = tk.Frame(root)#=============
frame.pack()#=======================
# DON'T WORRY ABOUT ANY OF THIS CODE

# Don't need this function if we use a lambda 
# def say_hi():
#     print("HELLO!")

button = tk.Button(frame, 
                   text="CLICK ME", 
                   fg="red",
                   command=lambda: print("Hello"))



# DON'T WORRY ABOUT ANY OF THIS CODE
button.pack(side=tk.LEFT) #=========
root.mainloop() #===================
# DON'T WORRY ABOUT ANY OF THIS CODE




# Example 2: Cube of anumber. This lambda takes a parameter and returns the cube of that number.  
                # The lambda itself is saved in the cube  variable.
cube = lambda num: num ** 3