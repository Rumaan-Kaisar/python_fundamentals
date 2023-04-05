# Capitalize strings using upper
    # Here are two potential solutions.  You can either capitalize each string as you add it to result:

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()
print(result)



# Or, you can add all strings to result, and then capitalize the whole thing once at the end.

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()
print(result)