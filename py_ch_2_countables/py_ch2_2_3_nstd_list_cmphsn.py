
# Courses: colt_py_bootcamps    117

# Multi-Dimensional lists are "nested list"
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing: nested_list[outer][inner], all possible way to access "second list, last element"
nested_list[1][-1]      # second list, last element
nested_list[-2][-1]     # second list, last element
nested_list[-2][2]      # second list, last element
nested_list[1][2]       # second list, last element

# Iterating through: 'number of loops' = 'number of nested layers'
for ls in nested_list:
    for nm in ls:
        print(nm)

# ----------|    Nested List Comprehension    |----------
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[print(val) for val in ls] for ls in nested_list]
[[nm/2 for nm in ls] for ls in nested_list]     # [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0], [3.5, 4.0, 4.5]]

# another Example
# Note: you dont have to use the "List Comprehension variables", they can ony used to iterate
    # following doesn't use 'vat' or 'num' either to make the list-of-list
board = [[num for num in range(1, 4)] for val in range(1 , 4)] 
print(board) # [[1, 2, 3], [1, 2, 3],	[1, 2, 3]]

# list-of-list however following uses the "List Comprehension variables"
board2 = [[num+val for num in range(val-1, 1+val)] for val in range(1 , 4)] 
print(board2) # [[1, 2], [3, 4], [5, 6]]

# In following we uses some conditional logics
[["X" if (num%2 != 0) else "O" for num in range(1, 4)] for val in range(1, 4)]
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]
[[num if (num%2 != 0) else "O" for num in range(val*num, val*num + 3)] for val in range(1, 4)]

[['*' for x in range(1, 4)] for i in range(1, 4)]
[['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

# ----------|    Recap    |----------



