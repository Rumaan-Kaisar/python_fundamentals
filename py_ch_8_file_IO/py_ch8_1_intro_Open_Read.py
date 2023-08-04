
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



# -----------    FILIO in CLI    -----------

>>> f = open("story.txt")
>>> f
<_io.TextIOWrapper name='story.txt' mode='r' encoding='cp1252'>

>>> help(f)
# Help on TextIOWrapper object:

>>> print(f) # wont work, instead use read()

>>> f.read()
'This short story is really short.\n'
# Notice "\n" new-line, because in the documant, we have an empty line 



# If nothing is specified in read(), as argumnet, then "-1" will be used autometicaly
    # "-1" will return all the content




# ---------------    Different Modes    ---------------
""" 
    Character           Meaning
        'r'	        open for reading (default)
        'w'         open for writing, truncating the file first 
        'x'	        open for exclusive creation, failing if the file already exists
        'a'	        open for writing, appending to the end of the file if it exists

        'b'	        binary mode
        't'	        text mode (default)
        '+'	        open a disk file for updating (reading and writing)

        'U'	        universal newlines mode (deprecated)

"""




# ---------------    Cursor Movement    ---------------

# Python reads files by using a "CURSOR"
# This is like the cursor you see when you're TYPING
# After a file is read, the cursor is at the END

# Note that, once we read the whole file using f.read()

# a "cursor" moves to the end of the file.
    # using f.read() again will give an "Empty-String"
    # New content shown if new content added to the "txt/file"
        # will show ther content from the previous position of the cursor


