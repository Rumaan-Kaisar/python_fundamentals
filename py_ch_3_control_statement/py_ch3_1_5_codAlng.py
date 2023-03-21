# Courses: colt_py_bootcamps     89, 90

# ---------|    String Multiplication    |---------
# Example 1:  print using nested "for" and "while" loop
# Notice: "String" is multiplied by a "number"
# With a for loop
for x in range(3):
	for num in range(1,11): 
		print("\U0001f600" * num)

# With a while loop
times = 1
while times < 11:
	print("\U0001f600" * times)
	times += 1

# Centered characters
times = 1
while times < 20:
	print(" "*(19-times)+"\U0001f600" * times)
	times += 2

# Without string multiplication - ugly solution
for num in range(1,11): 
	count = 1
	smileys = ""
	while count <= num:
		smileys += "\U0001f600"
		count += 1
	print(smileys)
 


# Example 2: annoying copying sibling
msg = input("Say Something: ")


while msg != "stop copying me":
	print(msg)
	msg = input()
print("UGH FINE YOU WIN, BROTHER!")


# Refactored version
# while msg != "stop copying me":
# 	msg = input(f"{msg}\n")
# print("UGH FINE YOU WIN, BROTHER!")
