
# Courses: colt_py_bootcamps    355


# we've use sub() for substitute and replace
    # now we use it for swap items

    # we have a list of movie/book title with publishing year
        # we wand the year at the first og the title

import re
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]

#  if we use built-in sort method, it will sort the list alphabetically
    # but we want to sort w.r.t. publishing year
        # e.g "1987 - Significant Others"

titles.sort()
# print(titles)

# pattern (attempt 1): groups "title" & 'date'
pattern = re.compile(r'^[\w ]+ \(\d{4}\)')
# Notice the extra sapce '[\w ]+ '
    # if we use '[\w ]+' with no extara space, it will match 
        # 'Significant Others ' untill the '('
        # so after we swap, we'll endup a file name with space at the end
        # Grouping will help us to better organize

# pattern (attempt 2): groups "title" & 'date'
pattern = re.compile(r'(^[\w ]+) (\(\d{4}\))')
result = pattern.sub("\g<2> - \g<1>", titles[0])
print(result)   # (1987) - Significant Others

# pattern (attempt 3): groups "title" & 'date'
    # to avoid () we group only the 4-digits
pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
result = pattern.sub("\g<2> - \g<1>", titles[0])
print(result)   # 1987 - Significant Others


# pattern (attempt 4): now we run through all the titles
fixed_titles = []
pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')

for book in titles:
    result = pattern.sub("\g<2> - \g<1>", book)
    fixed_titles.append(result)

fixed_titles.sort()
print(fixed_titles)


# pattern (attempt 5): using the group names
fixed_titles = []
pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')

for book in titles:
    result = pattern.sub("\g<date> - \g<title>", book)
    fixed_titles.append(result)

fixed_titles.sort()
print(fixed_titles)




# -------------    instructor codes    -------------

import re
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]
titles.sort()
fixed_titles = []

pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')
for book in titles:
    # result = pattern.sub("\g<2> - \g<1>", book)
    result = pattern.sub("\g<date> - \g<title>", book)

    fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)






# Mode Solution
# This is another trickier exercise.  Don't feel bad if you were unable to complete it!

# I start by defining the function, which accepts a single argument we'll call collection .

# Next, I create a new dictionary that maps items in the collection to the number of times they appear in the collection. I used a dictionary comprehension along with count()  to achieve this.

# count = {val: collection.count(val) for val in collection}
# If collection was the string "happy", the resulting count dict would look like this:

# {
#     'h': 1, 
#     'a': 1, 
#     'p': 2, 
#     'y': 1
# }

# Now, I just need to find the maximum number in all the values (2 in my example).  To do that, I use

# max_value = max(count.values())
# Now we know what the maximum value is, we just have to find the corresponding key. (we have 2, and need to work backwards to find 'p').  This is harder than you might think.

# I convert the values in the dict to a list.  I do the same thing to all the keys.  Then, I find the index of max_value in the values and use that to access the corresponding key.

# #find index of max_value in the values
# correct_index = list(count.values()).index(max_value)
# #use that index to find the correct key
# return list(count.keys())[correct_index]
# Here is the complete code:


def mode(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]


