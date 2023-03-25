# Courses: colt_py_bootcamps    91

# "break" is used to exit a loop.

# following is an infinite loop, but we can exit this loop using "break"
while True:
    command = input("Type 'exit' to exit: ")
    if (command == "exit"):
        break



# following is a for loop, using "break" we exit the loop before it completes
for x in range(1, 101):
    print(x)
    if x == 3:
        break



# Another example: (previous codealong)
times = int(input("How many times do I have to tell you? "))

for time in range(times):
	print("CLEAN UP YOUR ROOM!")
    # Exit after fourth iteration
	if time >= 3: 
		print("do you even listen anymore?")
		break


# python py_ch3_2_1_break.py