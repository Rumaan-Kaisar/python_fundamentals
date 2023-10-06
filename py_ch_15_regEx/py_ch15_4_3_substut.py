
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





# -----------    usage of CAPTURE GROUP in sub()    -----------
    # point a group using 'number' or 'name'


# Example 2: Removing names and replace them in their first letter
                # e.g. Mrs. Daisy to Mrs. D. and Mr. White to Mr. W.
import re 
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"
pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([A-Za-z]+)", re.I)

# using sub() to REPLACE the matches
    # point to the group (Mr\.|Mrs\.|Ms\.) using "number"
result= pattern.sub('\g<1> REDACTED', text) # prints 'Mr\Mrs\Ms' + 'REDACTED'
print(result)   # Last night Mrs. REDACTED and Mr. REDACTED murdered Ms. REDACTED

# it's matching whatever the first group was
result= pattern.sub('REDACTED \g<1>', text) # prints 'Mr\Mrs\Ms' + 'REDACTED'
print(result)   # Last night REDACTED Mrs. and REDACTED Mr. murdered REDACTED Ms

# no group 
result= pattern.sub('REDACTED', text) 
print(result)   # Last night REDACTED and REDACTED murdered REDACTED


# To 'capture the first letter' we can modify our pattern 
pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
# the second group captures the first letter only, notice no '+' is used
result = pattern.sub("\g<1> \g<2>", text)
print(result)




# -------------    instructor codes    -------------
import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)
print(result)




# Example 3: Profanity Filter
                # My regex is pretty simple:

                #           \bfrack\w*\b

                # It looks for a word boundary and then the letters "frack" and then optionally more word characters afterwards, 
                    # and then a word boundary again. 

                # I used the word boundaries to prevent false positives if the "frack" occurs in the middle of another words

                # Here's the complete solution.  Notice I used the re.IGNORECASE flag:

import re

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)

print(censor("What the frack are you talkin about? I'm frakin exusted!! You're frakin dead... Frack! FRACK!!"))
