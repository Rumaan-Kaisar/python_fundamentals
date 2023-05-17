
# Courses: colt_py_bootcamps    209

# ---------------    raise    ---------------
# use "raise" keyword to make an exception (user created error)

# General form:
    #           raise ERR("ERR msg")

    # ERR could be any Error (must be listed in python) , but it must be Meaningful
    # "ERR msg" is the message that contain detailed error explanation

raise ValueError("OMG whtve u done!!")

raise TypeError("Holla!!")

raise TabError()    # None. since no message is used.

raise BlahBlah("Meh!")  # wont work




# Example 1: We can make our defined funstions more secure by using Exception
def colorize(text, color):
	colors = ("cyan", "yellow", "blue", "green", "magenta")
	if type(text) is not str:
		raise TypeError("text must be instance of str")
	if color not in colors:
		raise ValueError("color is invalid color")
	print(f"Printed {text} in {color}")

colorize([], 'cyan')
# colorize(34, "red")