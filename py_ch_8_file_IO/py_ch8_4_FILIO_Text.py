
# Courses: colt_py_bootcamps    308


# ---------------    FILIO : TextIO    ---------------
# we also use open() to "write" a file
    # we have to specify "w" flag


# Example 1: Write a text file
with open("haiku.txt", "w") as fL:
    fL.write("Writing files is great\n") 
    fL.write("Here's akother line of text\n")
    fL.write("Closing now, goodbye!")


# above code without using "with"
# file = open("haiku.txt", "w") 

# file.write("Writing files is great\n") 
# file.write("Here's akother line of text\n")
# file.write("Closing now, goodbye!")

# file.close()




# -------------   "w": Default is "overrite"   -------------
# when we're using "w" flag, default is ovveriting for "pre-existed" file
# Following ovverites the previous one
with open("haiku.txt", "w") as fL:
    fL.write("Oh no! We've lost all content!!\n") 
    fL.write("Boo Hoo!!\n") 

    



