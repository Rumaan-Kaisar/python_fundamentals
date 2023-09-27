
# Courses: colt_py_bootcamps    346

# --------------    Project    --------------

# -----    Attempt : 1    -----
# 'def extract_phone' will extract the phone numbers from a given string

import re
# Returns first instance of phone number pattern:
def extract_phone(input):
    phn_rgEx = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phn_rgEx.search(input)
    if match:
        return match.group()
    return None

print(extract_phone("my number is 432 567-8976"))
print(extract_phone("my number is 432 567-897622"))
print(extract_phone("432 567-8976 asdjhasd "))
print(extract_phone("432 567-8976"))



# Returns all instances of phone number pattern in a list
def extract_all_phones(input):
    phn_rgEx = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phn_rgEx.findall(input)
    if match:
        return match
    return None

print(extract_all_phones("my number is 432 567-8976 or call me at 345 666-7899"))
print(extract_all_phones("my number is 432 56"))




# -----    Attempt : 2    -----
# 'def is_valid_phone' will checks if th enumber is valid phone number

# validating inputs: useful for valdating emails, phone-nuumbers, credit-card no, and more.

is_valid("something mathed")    # True
is_valid("Not mathed")    # False

# we can accomplish this by using '^' and "$" at start and end of the pattern
    # ^ : means start with      $ : means end with
import re
def is_valid_phone(input):
    phn_rgEx = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phn_rgEx.findall(input)
    if match:
        return True
    return False

print(is_valid_phone("432 567-8976"))
print(is_valid_phone("432 567-8976 ads"))
print(is_valid_phone("asd 432 567-8976 d"))



# ------    fullmatch    ------
# instead of using '^' and '$' we can use fullmatch()
import re
def is_valid_phone(input):
    phn_rgEx = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phn_rgEx.fullmatch(input)
    if match:
        return True
    return False

print(is_valid_phone("432 567-8976"))
print(is_valid_phone("432 567-8976 ads"))
print(is_valid_phone("asd 432 567-8976 d"))

# If we use same pattern in different functions, 
    # then it's better to compile the pattern outside all the function




""" 
    Example 1: Time Validating
                The time must start with a digit, and there can be a second optional digit before the colon.  
                Then there's the colon and two mandatory digits.  
                    I used ^ and $ to make sure the time was the only thing in the input string.
                    The regular expression I used is: 

                        ^\d\d?:\d\d$

"""

import re 

def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False

print(is_valid_time("42:98"))
print(is_valid_time("12:60ads"))





# ------------    instructor code    ------------
import re
# Returns first instance of phone number pattern:
def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

# Returns all instances of phone number pattern in a list
def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

# One way of checking if entire string is valid phone number:
# def is_valid_phone(input):
# 	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
# 	match = phone_regex.search(input)
# 	if match:
# 		return True
# 	return False

# Another way of doing the same thing, using the fullmatch method
def is_valid_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False

# Calling our functions a bunch of times...

print(extract_phone("my number is 432 567-8976"))
print(extract_phone("my number is 432 567-897622"))
print(extract_phone("432 567-8976 asdjhasd "))
print(extract_phone("432 567-8976"))

print(extract_all_phones("my number is 432 567-8976 or call me at 345 666-7899"))
print(extract_all_phones("my number is 432 56"))

print(is_valid_phone("432 567-8976"))
print(is_valid_phone("432 567-8976 ads"))
print(is_valid_phone("asd 432 567-8976 d"))


