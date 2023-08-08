
# Courses: colt_py_bootcamps    309


# ---------------    FILIO : modes/flags    ---------------




# w - writes and erases existing contents
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# a - appends to end, preserving original contents
NO CONTROL OVER CURSOR
with open("haiku.txt", "a") as file:
	file.seek(0)
	file.write(":)\n")

# r+ read and write
with open("haiku.txt", "r+") as file:
	file.write(":)")
	file.seek(10)
	file.write(":(")

# r+ will not create a file if it doesn't exist
with open("hello.txt", "a") as file:
	file.write("HELLO!!!")





Copy Solution
Copy should copy contents from one file to another.  For example, after running:

copy('story.txt', 'story_copy.txt') # None
We would expect the contents of story.txt and story_copy.txt to now be the same.

Here's my solution:

def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)




Copy and Reverse Solution
copy_and_reverse  is very similar to the previous exercise, copy , except that we reverse the text using a slice before we write it to the new file:

def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])




Statistic Exercise Solution


def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }



Find and Replace Solution
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()

        
