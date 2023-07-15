# Courses: colt_py_bootcamps    86, 87

""" 
# Example 1: Following assertion makes sure that both numbers are positives

def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
	# assert	expression	,	error_msg
    return x + y

print(add_positive_numbers(1, 1)) # 2
add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive!
"""

# Example 2: Force to input listed junk-food
def eat_junk(food):
	assert food in [
		"pizza", 
		"ice cream", 
		"candy", 
		"fried butter"
	], "food must be a junk food!"
	return f"NOM NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))

# python test.py