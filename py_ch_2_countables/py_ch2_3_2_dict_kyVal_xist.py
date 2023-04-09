
# Courses: colt_py_bootcamps    127 

# ---------------|    How to check existance of key or value    |---------------

instructor = {
    "name": "Cbolt",
    "owns_dog": True,
    "numcourses": 4,
    "favorite_language": "Python", 
    "is_hilarious": False,
    44: "my favorite number !"
}

# check the keys
"name" in instructor    # True
"awesome" in instructor # False

# another way is to use 'in' with key() and values()
"name" in instructor.keys()    # True
"awesome" in instructor.keys() # False

4 in instructor.values()    # True
"my favorite number !" in instructor.values() # True


