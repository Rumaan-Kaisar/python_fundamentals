
# Courses: colt_py_bootcamps    304, 305

# ---------------    objectives    ---------------
    # Read text files in Python
    # Write text files in Python
    # Use "with" blocks when reading / writing files
    # Describe the different ways to open a file
    # Read CSV files in Python
    # Write CSV files in Python
    # Work with JSON




# ---------------    objectives    ---------------

# You can read a file with the 'open()' function
# open returns a file object to you:
    # The object not only contains the file but also the meta-data
    # Meta-data: file info, e.g. type of file, last access, last modofied etc
# You can read a file object with the 'read()' method


# open:
    # parameters: file-path, mode, buffering, encoding, reeors etc




# Example 1: Demo

# story.txt
This short story is really short.


# reading_files.py
file = open("story.txt") 
file.read()

2:57
