
# Courses: colt_py_bootcamps    228

# Previously we got all HTML
import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url)  # just gets HTML



# -------------    Specify HEADERS of "request"    -------------

import requests 

# specify the data using "key", EG: "headers"
res = requests.get("https://www.example.com", headers = {
    "header1": "value1",
    "header1": "value1"
    }
)




# Example 1: Request a plain text.

import requests
url = "https://icanhazdadjoke.com/"


# Plain Text: ask for plain text
response_1 = requests.get(url, headers={"Accept": "text/plain"})
# "headers" is used to specify multiple keywords
print(response_1.text)  

# HTML: ask for HTML by sepcifying in "request header"
response_2 = requests.get(url, headers={"Accept": "text/html"})
print(response_2.text)  



# ----------------    JSON : JavaScrpt Object notation    ----------------

# Example 2: Request JSON.

import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

print(response.text)    # prints the JSON string
# usually the given data is in STRING format: "{...}"
print(type(response.text))      # class <'str'>


# Follwing converts the JSON string into valid Python - Dictionary
print(type(response.json()))    # class <'dict'>
data = response.json()
print(data)

print(data["joke"])
print(f"status: {data['status']}")






# To get "PLAIN TEXT"


