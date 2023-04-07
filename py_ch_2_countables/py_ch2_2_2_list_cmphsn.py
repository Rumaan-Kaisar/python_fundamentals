
# Courses: colt_py_bootcamps    111,  112

# --------------|    LIST COMPREHENSION    |--------------
# It is applied to many Data-Structures: Dictionaries, Sets, Tuples, Generators
# Synatax:      [ __  for  __  in  __ ]
# [ first_var_name  for  second_var_name  in iterables_list_range ]

nums_a = [1, 2, 3]
nums_10 = [x**2 for x in nums_a]    # [1, 4, 9]

# Following is equivalent loop and list comprehension
numbers_a = [1, 2, 3, 4, 5] 
doubled_numbers = []
for num in numbers_a:
    doub_num = num * 2 
    doubled_numbers.append(doub_num)
print(doubled_numbers) # [2, 4, 6, 8, 10]

dbl_nums = [numb*2 for numb in numbers_a] # list comprehension
print(dbl_nums) # [2, 4, 6, 8, 10]



# list comprehension with strings
name = "Satoru"
[ch.upper() for ch in name]     # ['S', 'A', 'T', 'O', 'R', 'U']

friends = ['ashley', 'matt', 'michael']
[friend[0].upper() for friend in friends]   # ['A', 'M', 'M']
[friend[0].upper()+friend[1:] for friend in friends]   # ['Ashley', 'Matt', 'Michael']



# list comprehension with range
[num*15 for num in range(1, 10, 2)]     # [15, 45, 75, 105, 135]
# range(1, 10, 2) is  [1, 3, 5, 7, 9]



# list comprehension with Bolians, Truthy-Falsy check
[bool(val) for val in ["", '', False, True, "0", 1, 0, []]]
# [False, False, False, True, True, True, False, False]



# list of numbers converted into strings
[str(num) for num in [1, 2, 3, 4, 5]]   # ['1', '2', '3', '4', '5']

# convert uppercase
colors = ['red',	'orange',	'yellow',	'green',	'blue',	'indigo']
[color.upper() for color in colors]     # ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO']







# --------------|    LIST COMPREHENSION with Logic    |--------------
# combine conditions at the end of the LIST COMPREHENSION
# using 'if'
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num%2 == 0]
print(evens)    # [2, 4, 6]
odds = [num for num in numbers if num%2 != 0]
print(odds)     # [1, 3, 5]

# using 'if-else'
[num*2 if num%2 == 0 else num/2 for num in numbers] # [0.5, 4, 1.5, 8, 2.5, 12]
# i.e if even, num*2, otherwise num/2

# using 'in' to combne the condition: following 2 'in's are used
with_vowels = "This is so much fun!"
''.join(char for char in with_vowels if char not in "aeiou" )   # "Ths s s mch fn!"
        # ListComprehension iterable: char in with_vowels
        # ListComprehension's condition iterable: char not in "aeiou"
# following also works with []
''.join([char for char in with_vowels if char not in "aeiou"])

# Note: join(), takes one argument- as a list
" ".join(['OMG.', 'Oh no.'])
"__".join(['OMG.', 'Oh no.'])

[char for char in with_vowels if char not in "aeiou"]
# ['T', 'h', 's', ' ', 's', ' ', 's', ' ', 'm', 'c', 'h', ' ', 'f', 'n', '!']


# --------------|    More practice o List Comprehension    |--------------
[person[0] for person in ["Elie", "Tim", "Matt"]]   # ['E', 'T', 'M']
[val for val in [1,2,3,4,5,6] if val%2 == 0]    # [2, 4, 6]

# Using good old manual loops:
answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])
print(answer)   # ['E', 'T', 'M']

answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)
print(answer2)  # [2, 4, 6]




# Reversing example

# Using list comprehensions(the more Pythonic way): 
answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

# Without list comprehensions, things are a bit longer:
# find common items
answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
print(answer)   # [3, 4]

answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())
print(answer2)  # ['eile', 'mit', 'ttam']

# Nice and short using a list comprehension 12's products: 
answer = [val for val in range(1,101) if val % 12 == 0]




# Elminate vowels
# Using a string (preferable solution):
[char for char in "amazing" if char not in "aeiou"] 

# Using a list:
[char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]] 




# Example of generatinf list-of lists (ulti-dim) using "list comprehension"
answer = [[i for i in range(0,3)] for num in range(0,3)]
print(answer)

'''
To generate the following using a nested list comprehension:
[
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 ]
My solution looks like this:
'''

answer = [[i for i in range(0,10)] for num in range(0,10)]
print(answer)

