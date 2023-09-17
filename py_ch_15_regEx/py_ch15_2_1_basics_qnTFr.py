# Courses: colt_py_bootcamps    341

# ----------------    Quantifers    ----------------
# Group 2 : RegEx Syntax
""" 
        +       One or more
        {3}     Exactly x times. {3}-3 times
        {3,5}   Three to five times
        {4,}    Four or more times
        *       Zero or more times
        ?       Once or none (optional)
"""
# these specifies how many times something should ocuurs 'in a pattern'

# ------------------ test string --------
hello world aaabbbcccdddeeef ffggg 
I like cats and kittens :)
PURPLE
kitty@gmail.com
She is 49 years old. I am 75 years old. He is 3 3.
# ---------------------------------------

# -----    +  : one or more    -----
# Select "Any word start with k"
# use: 'k\w+', (using only 'k\w' only selects 2-letters). 'ke' is selected from 'like'
    # better : '\sk\w+' selects words only starts with 'k'

