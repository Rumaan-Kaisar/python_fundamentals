
# Courses: colt_py_bootcamps    309


# ---------------    FILIO : modes/flags    ---------------
""" 
    Modes for Opening Files
        r   - Read a file (no writing) - this is the default 

        w   - Write to a file (previous contents removed) 

        a   - Append to a file (previous contents not removed) 
                append at the end 
                no cursor control
                file created if doesn't exist 

        r+  - Read and write to a file (writing based on cursor) 
                OVERRITE the text from start
                ERR if file doesn't exist
                append from start
                cursor control
"""


# w - writes and erases existing contents
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")



# a - appends to end, preserving original contents
# NO CONTROL OVER CURSOR
with open("haiku.txt", "a") as file:
    file.seek(0)    # it has no effect for "a-append" mode
    file.write("\n This is APPENDED!!!\n")
    file.write(":)\n")  # always append at the end



# r+ read and write
    # overrite the text from start
    # seek/cursor works
with open("haiku.txt", "r+") as file:
    file.write("OVERRITtEn")
    file.write(":)")
    file.seek(10)
    file.write(":(")

# output: OVERRITtEn:(s is great



# r+ will not create a file if it doesn't exist
# with open("hello.txt", "r+") as file:      #ERR
with open("hello.txt", "a") as file:
    file.write("HELLO There !!! How ya doin?")




# Example 1: Copy should copy contents from one file to another.  
            # For example, after running:   copy('story.txt', 'story_copy.txt')     # None
            # We would expect the contents of 'story.txt' and 'story_copy.txt' to now be the same.

def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)

copy('story.txt', 'story_copy.txt')




# Example 2: Copy and Reverse the content. It is very similar to the previous exercise, 
            # we reverse the text using a slice before we write it to the new file:

def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])  # reverse the text then write

copy_and_reverse('story.txt', 'story_copy_N_rev.txt')
# last line becomes first
# each line is reversed




# Example 3: Statistic of a file word, lines, characters.
def file_statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()    # all lines in a list

    return { 
        "lines": len(lines),
        "words": sum(len(line.split(" ")) for line in lines),
        "characters": sum(len(line) for line in lines) 
        }

file_statistics("story.txt")    # {'lines': 3, 'words': 13, 'characters': 69}




# Example 4: Find and Replace words of a file
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()  # store the old text
        new_text = text.replace(old_word, new_word)     # change the text
        file.seek(0)        # cursor reset is needed because we used read()
        file.write(new_text)    # write changed text
        file.truncate()     # resizes the file

find_and_replace("hello.txt", "HELLO", "Oy")


# ------------    Python File truncate() Method    ------------
    # The truncate() method resizes the file to the given number of bytes.
    # If the size is not specified, the current position will be used.

""" 
Syntax:
        file.truncate(size)

    Parameter
        size: The size of the file (in bytes) after the truncate. Default None, which means the current file stream position.
"""        

