
# Courses: colt_py_bootcamps    111

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


