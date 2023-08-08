
# Courses: colt_py_bootcamps    307


# ---------------    with-block FILIO    ---------------

# Option 1: Manual Open-Close
file = open("story.txt") 
file.read() 
file.close()
file.closed # True


# Option 2: auto closed file after exiting "with-block"
with open("story.txt") as file: 
    file.read()

file.closed # True




# Example 1 : store content to a variable. CLI demo:
with open("story.txt") as f:
    data = f.read()

>>> with open("story.txt") as f:
...     data = f.read()
...
>>> f
<_io.TextIOWrapper name='story.txt' mode='r' encoding='cp1252'>
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> f.closed
True
>>> data
"This short story is really short.\nNow it's a little longer.\nThe end.\n"




# --------------    with : what's going under the hood?    --------------
    # When enter the "with-block" the f.__enter__() method is called
    # when exit the "with-block" f.__exit__() method is called

    # it's not limited to FILE-IO
        # __enter__() and __exit__() is called for any block/class when we use "with"

# f.__enter__() canbe used after a file opened "f = open("story.txt")"



# Example 2: following mimics the "with" in CLI
>>> f = open("story.txt")
>>> f.__enter__()   # simeilar to enter 'with-block'
<_io.TextIOWrapper name='story.txt' mode='r' encoding='cp1252'>
>>> f.read()
"This short story is really short.\nNow it's a little longer.\nThe end.\n"
>>> f.closed
False
>>> f.__exit__()    # closes the file. simeilar to exit 'with-block'
>>> f.closed
True

