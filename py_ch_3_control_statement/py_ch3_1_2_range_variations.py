

# Courses: colt_py_bootcamps    84

# ----------    range()_ variations    ----------
# Creates "immutable" sequence of numbers
range(6)    # Exclude endpoint, creates 0, 1, . . ., 5
range(6, 12)    # Exclude endpoint, creates 6, 7, . . ., 11
range(14, 8, -2)    # With steps, Exclude endpoint, creates 14, 12, 10

for i in range(14, 8, -2):
    print(i)    # prints 14, 12, 10

# use list to convert these sequence to lists

sq1 = range(6)
sq2 = range(6, 12)
sq3 = range(14, 8, -2)

ls1 = list(sq1)
ls2 = list(sq2)
ls3 = list(sq3)

print(ls1)
print(ls2)
print(ls3)