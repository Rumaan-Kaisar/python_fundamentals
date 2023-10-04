
# Courses: colt_py_bootcamps    353


# ----------    substitution    ----------
# Find (search) and replace things in regEx, based on a "pattern"

# Sometimes we can do it without regEx. e.g. using "STRING methods"
    # str.replace(old, new[, count])
        # Returft a copy of the string with all occurrences of substring old replaced by new.
    # used for:
        # replace f-words with ***
        # Hide user info (e.g. phn no.)

# But there are some cases that we have to use "regEx"



# -------------    regEx sub()    -------------
# ptrn.sub("word", "text where replace happens")
import re

ptrn = re.compile(r"blue|white|red")
ptrn.sub('colour', 'blue socks and red shoes') # 'colour socks and colour shoes'




# Example 1: Removing names in a text
import re 
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

# Apply IgnoreCase
# Technically the periods '.' should be escaped so that they only match periods:
    # (Mr\.|Mrs\.|Ms\.)

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([A-Za-z]+)", re.I)
print(pattern.findall(text))    # find all matches
print(pattern.search(text).group())    # find first match
print(pattern.search(text).groups())    # find first match and show in group-touple

# using sub() to REPLACE the matches
result= pattern.sub('REDACTED', text) 
print(result)
