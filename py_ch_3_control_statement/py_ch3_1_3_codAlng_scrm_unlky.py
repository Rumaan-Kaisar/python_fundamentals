# Courses: colt_py_bootcamps    86, 87

# ----------| Scream to Clean  |----------
times = input("How many times do I have to tell you? ")
times = int(times)

# Simplest Version
for time in range(times):
	print("CLEAN UP YOUR ROOM")

# Version 2
for time in range(times):
	print(f"time {time+1}:CLEAN UP YOUR ROOM")



# ----------| for 1-21; 4, 13 print Unlucky, Others: Even, Odd  |----------
# Note:	Order matters, first check "Unlucky" to avoid "Even"

	# Main Solution
for num in range(1,21):
	if num == 4 or num == 13:
		print(f"{num} is unlucky")
	elif num % 2 == 0:
		print(f"{num} is even")
	else:
		print(f"{num} is odd")

	
# Slight Refactor: avoid print statement
for num in range(1,21):
	if num == 4 or num == 13:
		state = "unlucky"
	elif num % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{num} is {state}")