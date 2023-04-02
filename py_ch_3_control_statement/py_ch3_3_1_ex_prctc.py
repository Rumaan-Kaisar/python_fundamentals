# Solution Using a Conditional
    # This solution loops over all the numbers between 10 and 20, 
    # checking to see if the number is even inside the loop.

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n


# Solution using range step
    # Instead of looping over every number between 10 and 20, this solution only loops over the odd numbers.  
    # Remember, the 3rd argument to range() is the "STEP" or interval that you want the range to increment by.

x = 0

for i in range(11,21,2):
        x += i


# counts the iteration untill 5 is founf from randint(1, 10)
from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 #store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5: #keep looping while number is not 5
    i += 1
    number = randint(1, 10) #update number to be a new random int from 1-10