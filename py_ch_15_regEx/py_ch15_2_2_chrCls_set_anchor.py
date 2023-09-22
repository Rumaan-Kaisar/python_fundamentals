
# Courses: colt_py_bootcamps    342, 343

# ------------------ test string --------
hello world aaabbbcccdddeeef ffggg 
I like cats and kittens :)  415 4129876
PURPLE 415 412-9876
kitten@gmail.com LOL
310 467-9876
She is 49 years old. I am 75 years old. He is 3 3.
# ---------------------------------------


# -------------    Character Class : usage of []    -------------
# specify :
    # group of characters 
    # ranges of characters

# 'aeiou' matches the exact strings.
# [aeiou] matches anything built with any of these letters
    # e, a, aa, eaea etc

# To match double vowles:   [aeiou]{2}
    # selects: aa, ee, ai, au, ea, ae etc. Finding any two vowels next to one another

# It is CASE SENSITIVE


# -----    ranges    -----
# select all lower-case letter: [a-z]
# select all upper-case letter: [A-Z]

# select all twwo or more upper-case letter: [A-Z]{2,}


# combinations:
    # any lowercase or numbers:  [a-z0-9]


# AVOID: to avoid a letter or ranges, use '^'
    # any letter but 'k': [^k]
    # anythin but 0-9 and "aeiou": [^0-9aeiou ]
    # we can also avoid any specilal characters eg. '@': [^0-9aeiou @]




# -----------    Anchors and Boundaries    -----------
""" 
    ^	Start of string or line
    $	End of string or line
    \b	Word boundary 
"""

# ^:
    # Cosider we want to extuct phone numbers we used: '\d{3} \d{3}-?\d{4}'
        # it selects: '415 412-9876' form any kind of thext: e.g.
        # wkuydgbaseuy415 412-9876wdvrtgn

    # Now we want to add a restriction: 'the line has to start with a phone number'
        # in this case we use : '^\d{3} \d{3}-?\d{4}'
            # notice '^' at the beggining


# $: 
    # 'the line has to end with a phone number' : '\d{3} \d{3}-?\d{4}$'
    # To search a phone nuber, nothing but in a single line
    # '^\d{3} \d{3}-?\d{4}$'  : means line statrt with a phone number and ends withs phone number
    # only "*** ***-****" pattern (nothging else)
    # useful to verify: "only email", "specific serial key pattern"



# -----------    word boundery    -----------
# selects the word between bounderies : (e.g. space, back-slash, new-line etc)
    # selects only words: '\b\w+\b'

