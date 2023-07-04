
# Courses: colt_py_bootcamps    275

# ----------------    fibonacci sequence    ----------------

# =-=-=-=-=-=    WITHOUT A GENERATOR    =-=-=-=-=-=

# Example 1: following returns list of fibonacci numbers, where list length is "max"

def fib_list(max):
    nums = []
    a, b = 0, 1

    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

print(fib_list(10))	 # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# As above, to get n-th fibonacci numbers, we have to calculate previous (n-1) numbers
fib_list(1000000)
# this would take more-memory in the RAM (400mb)
# thats why we need to use GENERATOR




# =-=-=-=-=-=    USING A GENERATOR    =-=-=-=-=-=
# in this case only 6.5mb is used to calculate it (for list it was 400mb)
# Hence GENERATOR will save huge amount of memory.

# Example 2: above example but this time we'll use a GENERATOR
                # To generate first 1,000,000 fib numbers, no list needed!
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1


# prints one million fibonacci numbers
for n in fib_gen(1000000):
	print(n)




# Example 3:  Get Multiples Generator 

def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num

mult_res = get_multiples(2, 10)

for i in mult_res:
	print(i)




# Example 4 : Get Unlimited Multiples
            # This is similar to previous exercise, except it's simpler! 
                # We just loop forever (while True) instead of checking to see how many times we've looped.

def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num

mult_unltd = get_unlimited_multiples(2)

for i in mult_unltd:
	print(i)
