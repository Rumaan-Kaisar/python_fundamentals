
# Courses: colt_py_bootcamps    179

# -------------------    Parameter oredering    ------------------- 
    # Always maintain following order when defining a function

            #   parameters
            #   *args
            #   default parameters
            #   **kwargs



# Example 1: Order of different kind of parameters
def display_info(a, b, *args, instructor= "Mahem", **kwargs):
    # print(type(args))
    return [a, b, args, instructor, kwargs] 

print(display_info(1, 2, 3, last_name="Inkerro", job="Instructor"))
# [1, 2, (3,), 'Mahem', {'last_name': 'Inkerro', 'job': 'Instructor'}]

    #	a - 1
    #	b - 2
    #	args (3)
    #	instructor - "Mahem"
    #	kwargs - {'last_name': "Inkerro", "job": "Instructor"}


# Single item tuple:
    # (3) is not cosidered as single item tuple.
    # we nees to add a comma after the item to notify Python, that it is a tuple with single item:
(3,)  # is a tuple
