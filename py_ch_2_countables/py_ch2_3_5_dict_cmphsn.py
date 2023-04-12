
# Courses: colt_py_bootcamps    134 

# ---------------|    Dict comprehension    |---------------

# Syntax:   {_:_ for _ in _}
# Notice the : , '_:_' acts as key-value pair in the new dictionary.
# iterates over keys by default
# iterates over "keys" and 'values if we use .items()

# Example 1: making new Dict from a Dict
numbers = dict(first = 1, second = 2, third = 3)

sqr_nums = {key : val**2 for key, val in numbers.items()}
print(sqr_nums)     # {'first': 1, 'second': 4, 'third': 9}



# Example 2: Making new Dict from a list
{num: num**2 for num in [1, 2, 3, 4, 5]}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



# Example 3: Combining two strings into a Dict
str1 = "ABC"
str2 = "123"
combo = {str1[i] : str2[i] for i in range(0, len(str1))}
print(combo)    # {'A': '1', 'B': '2', 'C': '3'}


instructor = {'name': 'coblt', 'city': 'san francisco', 'color': 'purple'}
yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}
# {'NAME': 'COBLT', 'CITY': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}



# ---------------|    Dict comprehension with LOGIC   |---------------
num_list = list(range(1, 6))

evn_odd = {num: ("even" if num%2 == 0 else "odd") for num in num_list}
print(evn_odd)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

{ num : ("even" if num % 2 == 0 else "odd") for num in range(0, 100)}

instructor = {'name': 'coblt', 'city': 'san francisco', 'color': 'purple'}
yelling_instructor = {(k.upper() if k == "color" else k) : v.upper() for k,v in instructor.items()}
print(yelling_instructor)
# {'name': 'COBLT', 'city': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}