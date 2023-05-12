
# Courses: colt_py_bootcamps    202, 203, 204, 205, 206

# -----------------    zip    -----------------









midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
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



Interleaving Strings Solution
Here's a detailed walkthrough.  I know it can be overwhelming, but try to step through one piece at a time if you get stuck.

I start by defining interleave , which accepts 2 strings: str1, and str2
To make this easier, let's use an example. Let's say that I call interleave('hi', 'no') 
Focus on the innermost bit first. I zip the two strings together, which returns a list of tuples like: [('h','n'), ('i','o')] 
To get it back into a string, I need to:
First join the individual tuples into strings, which is what the first join()  does
it results in a list of strings: ['hn', 'io'] 
Finally, join all the remaining strings into one large string
results in 'hnio' 
Return the result!


def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))




Triple and Filter Solution
For my solution, I chose to use map and filter in combination.

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))





Extract Full Name Solution
I use map and a lambda to create a new list full of formatted strings:



def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
