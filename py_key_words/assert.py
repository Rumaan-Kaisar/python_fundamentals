''' 
Definition and Usage

#   The "assert" keyword is used when "debugging" code.
#   The "assert" keyword lets you 'test if a condition in your code returns True', if not, the program will raise an "AssertionError".
#   You can write a message to be written if the code returns False, check the example below. 
'''

x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"

# AssertionError: x should be 'hello'

y = "below"

#if condition returns True, then nothing happens:
assert y == "below"

#if condition returns False, AssertionError is raised:
assert y == "goodbye"

