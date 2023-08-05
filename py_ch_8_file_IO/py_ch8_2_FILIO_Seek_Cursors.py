
# Courses: colt_py_bootcamps    306


# ---------------    Cursor Movement    ---------------

# Python reads files by using a "CURSOR"
# This is like the cursor you see when you're TYPING
# After a file is read, the cursor is at the END

# Note that, once we read the whole file using f.read()

# a "cursor" moves to the end of the file.
    # using f.read() again will give an "Empty-String"
    # New content shown if new content added to the "txt/file"
        # will show ther content from the previous position of the cursor




# ---------------    seek()    ---------------
# Python File seek() method changes the file position
    # i.e. we can move the "cursor" anywhere using seek()

""" 
    The seek() method sets the current file position in a file stream.
    The seek() method also returns the 'new postion'.

    Syntax:
                file.seek(offset)

    Parameter:
        offset: A number representing the position to set the current file stream position. 
"""


# "story.txt": first we'll save the following text into a text-fioe called "story.txt"
""" 
This short story is really short.
Now it's a little longer.
The end.

"""


# Example 1: Change the current file position to 4, and return the rest of the line:
f = open("story.txt", "r")
f.seek(4)   # 4
print(f.readline()) #  'short story is really short.'




# Example 2: Return the new position
f = open("story.txt", "r")
print(f.seek(4))    # 4




# Example 3: CLI demo of seek() method
>>> file = open("story.txt")

>>> file.seek(0)    # move the cursor to the beginning
0
>>> file.read()
"This short story is really short.\nNow it's a little longer.\nThe end.\n"
>>> file.read()
''

# setting seek-value to 1
>>> file.seek(1)
1
>>> file.read() # notice at the start "T" is gone 
"his short story is really short.\nNow it's a little longer.\nThe end.\n"

# setting seek-value to 50
>>> file.seek(50)
50
>>> file.read() # reads from 50-th index position 
"e longer\nThe end."




# ==========    review : full video & following    ========== 


    3: 29


# ---------------    readline()  and readlines()  ---------------
# readline():
Returns one line from the file

# You can return one line by using the readline() method

Python File readline() Method

Example
Read the first line of the file "demofile.txt":

f = open("demofile.txt", "r")
print(f.readline())
Definition and Usage
The readline() method returns one line from the file.

You can also specified how many bytes from the line to return, by using the size parameter.

Syntax
file.readline(size)
Parameter Values
Parameter	Description
size	Optional. The number of bytes from the line to return. Default -1, which means the whole line.
More examples
Example
Call readline() twice to return both the first and the second line:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
Example
Return only the five first bytes from the first line:

f = open("demofile.txt", "r")
print(f.readline(5))






>>> file.readline()
'This short story is really short.\n 

>>> file.readline()
"Now it's a little longer\n"

>>> file.readline()
'The end.'

>>> file.readline()
''



# readlines()
Returns a list of lines from the file
# Need to reset file position using seek(0)

Python File readlines() Method

Example
Return all lines in the file, as a list where each line is an item in the list object:

f = open("demofile.txt", "r")
print(f.readlines())
Definition and Usage
The readlines() method returns a list containing each line in the file as a list item.

Use the hint parameter to limit the number of lines returned. If the total number of bytes returned exceeds the specified number, no more lines are returned.

Syntax
file.readlines(hint)
Parameter Values
Parameter	Description
hint	Optional. If the number of bytes returned exceed the hint number, no more lines will be returned. Default value is  -1, which means all lines will be returned.
More examples
Example
Do not return the next line if the total number of returned bytes ar more than 33:

f = open("demofile.txt", "r")
print(f.readlines(33))


>>> file.seek(0)
0
>>> file.readlines()
['This short story is really short.\n', "Now it's a little longer\n", 'The end.']
>>> file.read()
''




