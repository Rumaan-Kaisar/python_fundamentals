
# Courses: colt_py_bootcamps    348, 350


# --------------    more regEx GROUPS    --------------

# following regex is found online
    # it matches any kind of URLs
    
    # 'https?://www\.[A-za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*'

    # r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)'

# notice:
    # optional s in 'https'
    # . as escape char
    # [A-za-z-]{2,256}  for Base-DOMAIN NAME allowing 2 to 255 characters & dashes
    # \.[a-z]{2,6} for .com, .net .io, from 2 to 6 letters
    # [-a-zA-Z0-9@:%_\+.~#?&//=]*  notice '*' at the end, it means OPTIONAL, 
        # its for URL directory/route, query-strings
        # e.g.  http://www.example.net/serch/?q=tacos
    # notice the grouping


# Following Grouping will help to extruct:
    # 'http' or 'https' protocols
    # base domain
    # query strings, other additional path/info
import re
url_regx = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regx.search("http://www.example.net/serch/asssddc/qewf")
print(match.group())    # prints the whole match
print(match.groups())    # groups() wwill return the grouped url in tuple
# ('http', 'www.example.net', '/serch/')

print(match.group())    # prints the entire match
print(match.group(0))    # also prints the entire match
print(match.group(1))    # prints the index 0 of match
print(match.group(2))    # prints the index 1 of match
print(match.group(3))    # prints the index 2 of match
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")



# we can also do the Grouping for the 'phone' numbers
    # to extract area-codes
    # to validate



# -------    INSTRUCTOR CODES    -------
import re

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
print(match.groups())
print(match.group())




# Example 1: Parsing Bytes 
                # My regex looks like this: eight 1s or 0s, surrounded by word boundaries on either side.

                #                           '\b[10]{8}\b'

                # Remember a word boundary is either a space or the start/end of a line.
                # Use findall()  rather than search(), to return a list of all matches.

import re

def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results

parse_bytes("aefwe 10010000 dfbv 11110101")     # ['10010000', '11110101']





# --------------    Symbolic Group Names    --------------
# Lebeling Groups:
    #               (?P<name>...)
    #               (?P<label>[pattern])
        
        # accessing labeled group   match.group("label")

    # e.g.          (?P<first>[A-Za-z]+)
        # access:   match.group("first")

    # Each 'group name' must be defined only ONCE


# Matching names
import re

def parse_name(input):
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input)
    print(matches.groups())
    print(matches.group())
    # accessing by LABEL
    print(matches.group('first'))
    print(matches.group('last'))

parse_name("Mrs. Tilda Swinton")




# Example 2: Date Parsing
                # Two digits followed by either a comma, slash, or period.
                # Then two more digits followed by either a comma, slash, or period.  
                # And then 4 more digits.  

                # parens are used to form capture groups for the 3 sections.

                #                   '^(\d\d)[,/.](\d\d)[,/.](\d{4})$'

                # Then, I simply referenced those capture groups using match.group(1) or match.group(2), etc.

import re

def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None

print(parse_date("45,45,7899"))



# python py_ch15_4_1_URLs_SmbGrpNames.py

