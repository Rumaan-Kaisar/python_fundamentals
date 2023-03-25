# Courses: colt_py_bootcamps    92 - 94


# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

# Note: "FOR loop" is no good for this game


# Without "break" version
import random

random_number = random.randint(1,20)  # numbers 1 - 20
guess = None

while guess != random_number:
	guess = input("Pick a number from 1 to 20: ")
	guess = int(guess)
	if guess < random_number:
		print("TOO LOW!")
	elif guess > random_number:
		print("TOO HIGH!")
	else:
		print("YOU WON!!!!")

print(random_number)




# With "break" version
import random

random_number = random.randint(1,100)  # numbers 1 - 100
guess = None

while True:
	guess = input("Pick a number from 1 to 100: ")
	guess = int(guess)
	if guess < random_number:
		print("TOO LOW!")
	elif guess > random_number:
		print("TOO HIGH!")
	else:
		print("YOU WON!!!!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,100)  # numbers 1 - 10
			guess = None
		else:
			print("Thank you for playing!")
			break

 

# python py_ch3_2_2_guessing_game.py