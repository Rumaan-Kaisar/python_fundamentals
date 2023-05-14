
# Courses: colt_py_bootcamps    202, 203

# -------------------    zip    -------------------

# it joins two iterables into a single iterator
# rturns a iterator od tuples: 

    # The zip() function returns a 'zip object', which is an "iterator of tuples" 
    # where the first item in each passed iterator is paired together, 
    # and then the second item in each passed iterator are paired together etc.

    # Iteraotr stops when the shortest input is exhusted
    # If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

# We can convert "zip object" into "list" or "dictionary"

# zip-objects ITERATES ONLY ONCE




# Example 1: Join two tuples together:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)   # <zip object at 0x000001A40B072D80>
list(x)     # [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]




# Example 2: zip two lists and then convert "zip object" into "list" or "dictionary"
first_zip = zip([5, 7, 8], [1,2,3,4] )  # notice the lists lengths are not equal
list(first_zip)     # [(5, 1), (7, 2), (8, 3)]
dict(first_zip)     # {5: 1, 7: 2, 8: 3}




# Example 3: zip 3-list togather
num_1 = [1, 2, 3, 5]
num_2 = [23.4, 56.8, 9, 90, 99.9, 100.2]
words = ["hi", 'lol', 'haha', ":)"]
zipped = list(zip(words, num_1, num_2))

print(zipped)       # [('hi', 1, 23.4), ('lol', 2, 56.8), ('haha', 3, 9), (':)', 5, 90)]

# However, we cannot create a Dctionary with 3 values
dict(zip(words, num_1, num_2))      # ERR: dictionary update sequence element #0 has length 3; 2 is required




# -------------------    UNPACKING a zip    -------------------
# we use * to unpack a zip, with zip()

itr_tup = [(5, 1), (7, 2), (8, 3)]      # an iterable of tuple
unPack = zip(*itr_tup)  # unpacking
list(unPack)    # [(5, 7, 8), (1, 2, 3)]

# another example
itr_tup_2 = [('hi', 1, 23.4), ('lol', 2, 56.8), ('haha', 3, 9), (':)', 5, 90)]
unPack_2 = zip(*itr_tup_2)      # unpacking
list(unPack_2)      # [('hi', 'lol', 'haha', ':)'), (1, 2, 3, 5), (23.4, 56.8, 9, 90)]




# Example 4: create a dictionary of highest mark: {'dan':98, 'ang':91, 'kate':78}
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
    # recall, a map takes a function (usually a lambda) and a iterable; 
    # then runs the function for each element of the iterable
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)


# another way
final_grd_2 = dict(zip(students, [max(pair) for pair in zip(midterms, finals)]))
# [pair for pair in zip(midterms, finals)]      # [(80, 98), (91, 89), (78, 53)]
# [max(pair) for pair in zip(midterms, finals)]     # [98, 91, 78]


# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)




# Example 5: Interleaving Strings Solution
    # Here's a detailed walkthrough.  I know it can be overwhelming, but try to step through one piece at a time if you get stuck.

    # I start by defining interleave , which accepts 2 strings: str1, and str2
    # To make this easier, let's use an example. Let's say that I call interleave('hi', 'no') 
    # Focus on the innermost bit first. I zip the two strings together, which returns a list of tuples like: [('h','n'), ('i','o')] 
    # To get it back into a string, I need to:
    # First join the individual tuples into strings, which is what the first join()  does
    # it results in a list of strings: ['hn', 'io'] 
    # Finally, join all the remaining strings into one large string
    # results in 'hnio' 
    # Return the result!

def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

print(interleave("hayo", "Silva"))  # 'hSaiylov'




# Example 6: Triple and Filter Solution
# For my solution, I chose to use map and filter in combination.
    # filter takes a function (usually a lambda) and a iterable

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))




# Example 7:    Extract Full Name Solution
# I use map and a lambda to create a new list full of formatted strings:

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l)) 
# or
def extract_full_name(l):
    return list(map(lambda val: f"{val['first']} {val['last']}", l))

