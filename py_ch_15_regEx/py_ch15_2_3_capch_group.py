
# Courses: colt_py_bootcamps    344


# -----------------    logical OR - |    -----------------
# Your test string:
# 415 345 0998 
# (415) 345 0998

# '\d{3} \d{3} \d{4}' only mathes the first string


# matching the paranthesis '()'
    # to mathc the '(415)' use:     '\(\d{3}\)'

# Selecting both string using OR '|'
    # In this case the OR is applied to whole-part "\d{3} \d{3} \d{4}":   '\(\d{3}\)|\d{3} \d{3} \d{4}'
    # To solve this we use "()" withot '\':  '(\(\d{3}\)|\d{3}) \d{3} \d{4}'




# ---------     more on PARAMS: Grouping     ---------
    # matching "Mr. Mrs. or Miss"

# Your test string:
# Mr. Luca Guadagnino 
# Mrs. Tilda Swinton

# Naieve Way:
'(Mr\.|Mrs\.) [A-Za-z]+[A-Za-z]+'

# we can however group these as below:
'(Mr\.|Mrs\.) ([A-Za-z]+[A-Za-z]+)'
# the benifit is: in Python the result will comes in two parts (as group)

# following has 3 groups: "Mr/Mrs", "First-name", "Last-name"
'(Mr\.|Mrs\.) ([A-Za-z]+) ([A-Za-z]+)'
# Notice the '+' are inside the '()'
# Makes esier to save those into DataBases
# to match URLS



# ---------    matching URLs    ---------
https://pythex.org
http://google.com

# 'https?://[A-Za-z_-]+\.[A-Za-z]+'

# However we can group the above, for better workflow in python.
# '(https?://)([A-Za-z_-]+\.[A-Za-z]+)'


