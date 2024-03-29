# Courses: colt_py_bootcamps 52 

# ------------ String Concatenation --------------

str_1 = "Waht"
str_2 = "the"
str_3 = str_1 + ' ' + str_2
print(str_3)

# ERR with contatenating non-string types
str_4 = 8 + str_1   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str_4)


# Concatenation operator "+="
str_5 = str_1 
str_5 += " "    # it is similar to str_5 = str_5 + " "
str_5 += str_2
str_5 += " "
str_5 += 'ice-cream !!'

print(str_5)



# Set the variable called greeting  to some greeting, e.g. "hello".
# Set the variable called name  to some name, e.g. "Heisenberg". 
# Then set the variable called greet_name  that that concatenates greeting , name , and a space " " between them.
greeting = "hello"

name = "Heisenberg"

greet_name = greeting + " " + name
