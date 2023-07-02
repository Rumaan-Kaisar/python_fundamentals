
# Courses: colt_py_bootcamps    273

# -------------    infnite generator    -------------

# Example 1: Infinite beat generator for drum playing
# no way to define a finction to do following without generator
	# Return a single number 
	# Every time different number
	# repeating

	# this is because we can return one thing from a function


# However we can define a Lame function that returns a list of beats.  
	# Only runs 100 times

# but its finite, and we dont want that

def current_beat():
	max = 100
	nums = (1,2,3,4)
	i = 0
	result = []
	while len(result) < max:
		if i >= len(nums): i = 0
		result.append(nums[i])
		i += 1
	return result

print(current_beat())

# also we could make the list bigger 10,000 or more
	# Then the memory will be used more, 
	# because as list grows it takes more memory
	# and we dont want the whole list, we want one thing at a time
	
	# in this case "Generator"  can help us




# Infinite Generator - returns one beat a time, no list used!
	# we don't need the giant list anymore
	# we can get one beat (number) at a time
def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1

cunter = current_beat()
next(cunter)

# for st in cunter:
# 	print(st)




# Example 2: Make a Song Generator
def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)


song = make_song()

print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
