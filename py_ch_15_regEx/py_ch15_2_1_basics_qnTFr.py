
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
I like cats and kittens :)  415 4129876
PURPLE 415 412-9876
kitten@gmail.com
310 467-9876
She is 49 years old. I am 75 years old. He is 3 3.
# ---------------------------------------

# -----    +  : one or more    -----
# Select "Any word start with k"
    # use: 'k\w+', (using only 'k\w' only selects 2-letters). 'ke' is selected from 'like'
    # better : '\sk\w+' selects words only starts with 'k'




# -----    {x} Exactly x times    -----
    # select a 5-letter long word 
    # '\s\w\w\w\w\w' or "\s\w{9}"

# matching digits of pattern '*** ***-****'
    # '\d{3} \d{3}-\d{4}'



# -----    range the occurance times: {3,5}   Three to five times    -----
    # select word characters between 5 to 7 characters 
    # "\w{5,7}"



# -----    lowwer bound: {4,}    -----
    # select all numbers having 3 or more digits:
    # "\d{3,}"



# -----    * : Zero or more times    -----
    # following selects: 'ac', 'abc', 'abbc', 'abbbc', 'abbbbc', ... etc
    # "ab*c"



# -----    ? : Once or none (optional)    -----
    # following selects 0 or 1 's': 'kitten' and 'kittens' but no 'kittenss'
    # "kittens?"

    # in following case '-' becomes optional
    # "'\d{3} \d{3}-?\d{4}'"

