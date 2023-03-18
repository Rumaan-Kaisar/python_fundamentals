
# Courses: colt_py_bootcamps    88

# --------| while |--------
# More careful with while Loop: Become infinete if no termination condition used

# Continues to ask for user input until the user types 'bananas'
msg = input("whats the secret password?")
while msg != "bananas":
	print("WRONG!")
	msg = input("whats the secret password?")
print("CORRECT!")


name = input("Inoput 'X' :")
while name != 'X':
    name = input("Inoput 'X' :")
print("done !!")


# for num in range(1,11):
# 	print(num)


# for num in range(33, 0, -1):
#     print(num)



# equivalent of above for loops
num = 1
while num < 11:
	print(num)
	num += 1

num = 33
while num > 0:
    print(num)
    num -= 1

