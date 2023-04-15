
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




# Courses: colt_py_bootcamps    135-138 (exercise)

# Example 1: Create a dictionary by using two list
    # use dictionary comprhnsn

# using Dictionary comprehension:
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0,3)}

# The "advanced" solution: using zip() method
dict(zip(list1, list2))  



# Example 2: Create a dictionary from a 2D-list (list of list)
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# method 1: If you have a "list of pairs", you can very easily turn it into a dictionary using dict() 
answer = dict(person)

# method 2: Using a dictionary comprehension and list indexes
answer = {thing[0]: thing[1] for thing in person}
# alternate solution:  without any references to list indexes:
answer = {k:v for k,v in person}



# Example 3: initialize using dictionary comprehension
{char:0 for char in 'aeiou'} 

# alternative: Using dict.fromkeys:
dict.fromkeys("aeiou", 0)



# Example 4: Use chr() on the numbers between 65 and 91:
answer = {count: chr(count) for count in range(65,91)}
""" {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 
    75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 
    85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'} """




