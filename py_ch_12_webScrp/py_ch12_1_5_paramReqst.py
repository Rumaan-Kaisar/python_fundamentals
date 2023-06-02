
# Courses: colt_py_bootcamps    229 

# -------------    Request with PARAMETERS : QUERY-string   -------------

# Query String: Pass Data to the SERVER
    # A way to pass data to the server as a part of a GET request
    # General form:
        # https://www.example.com/?key1=value1&key2=value2
        # use "?"
        # seperate key-val pair with "&"

    # Use the Query-String to get specific data from a server
        # Eg: search for a topic, get the data using Python



# -------------    Query String in Python    -------------
# Option 1:
import requests
response = requests.get("https://www.example.com/?key1=value1&key2=value2")


# Option 2:  Preferable way
import requests

response = requests.get(
    "https://www.example.com",
    params = {
        "key1" = "value1",
        "key2" = "value2"
    }
)




# Example 1 : Use Query-string to get data from API
# Note: first find the pattern by going in that website. Eg: searcing a Joke for specific topic "flower":
    # https://icanhazdadjoke.com/search?term=flower

import requests
url = "https://icanhazdadjoke.com/search"

# Always read 'API-Documentation' of a specific site
response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": "cat", "limit": 1}
    # above is similar to: 'https://icanhazdadjoke.com/search?term=cat&limit=1'
	# params={"term": "cat"}  # get all the Jokes of the specified topic, since 'limit' not specified
)


data = response.json()
print(data["results"])

# First grab the raw data and Analyze the keys, and then use that key
# print(data)

# note we can also do above thing using "Option-1", in that case we need to create a f-string

