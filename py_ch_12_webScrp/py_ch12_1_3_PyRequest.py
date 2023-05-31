

# Courses: colt_py_bootcamps    227

# ------------    requests    ------------

# pip install requests

import requests

# always use "https://" unless wont work
url_to_go = "https://news.ycombinator.com/"

res = requests.get(url=url_to_go)
# res = requests.get("https://news.ycombinator.com/")


print(f"Your request to {url_to_go} came back with STATUS code {res.status_code}")

print(res)
print(res.ok)
print(res.headers)  # shows the header of the HTML
print(res.content)  # Compact text: Shows the body or content of given HTML
print(res.text)     # Same as conent but slightly readable. Shows the body or content of given HTML




# Example 1: Send GET request to google.com
import requests
url = "http://www.google.com"
response = requests.get(url)

print(f"your request to {url} came back w/ status code {response.status_code}")

print(response.text)

