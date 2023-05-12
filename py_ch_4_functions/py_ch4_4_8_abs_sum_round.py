
# Courses: colt_py_bootcamps    198, 199, 200, 201

# -----------------    abs    -----------------


Greatest Magnitude Solution 
To find the greatest magnitude (the greatest distance from 0), I combine max() and abs()
I call abs() on each num, and find the maximum resulting value using max()


def max_magnitude(nums):
    return max(abs(num) for num in nums)




Sum Even Values Solution
I define a function called sum_even_values  which accepts any number of arguments, thanks to *args 
I grab the even numbers using the generator expression (arg for arg in args if arg % 2 == 0)  (could also use a list comp)
I pass the even numbers I extracted into sum()  and return the value
The default start value of sum()  is 0, so I don't have to do anything special to get it to return 0 if there are no even numbers!


def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)




Sum Floats Solution
Write a function called sum_floats. This function should accept a variable number of arguments. The function should return the sum of all the parameters that are floats. If there are no floats the function should return 0

I started by defining sum_floats , which accepts any number of arguments using *args 
Much like the previous exercise, I use a generator expression to extract the values in args where type()  is float.
I pass those values in to sum  and return the result


def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)


