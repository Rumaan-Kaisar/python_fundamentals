
# Courses: colt_py_bootcamps    327, 328

# ----------------    Beautiful soup    ----------------

# INSTALLING Beautiful soup
# pip install bs4
# This is a dummy package managed by the developer of Beautiful Soup to prevent name squatting. 
    # The official name of PyPI's Beautiful Soup Python package is "beautifulsoup4". 
    # This package ensures that if you type 'pip install bs4' by mistake you will end up with Beautiful Soup.

# Instead use:
    # pip install beautifulsoup4

# Beautiful Soup is a library that makes it easy to scrape information from web pages. 
    # It sits atop an HTML or XML parser, 
    # roviding Pythonic idioms for iterating, searching, and modifying the parse tree.



# --------------    Getting started with Beautiful Soup    --------------
# To extract data from HTML, we'll use Beautiful Soup
# Install it with pip
# Beautiful Soup lets us navigate through HTML with Python
# Beautiful Soup does NOT download HTML - for this, we need the 'requests' module!

# generally space each request by 3 seconds
    # grab the HTML, scrape it using "Beautiful Soup"




# ---------------    Parsing and Navigating HTML    ---------------

# Initialize 'Beautiful Soup' after we import it using
    # BeautifulSoup(html_string, "html.parser")
        # we have to specify "html.parser" because Beautiful Soup also works with XML
    # since, the html is sent us as a giant string
        # it checks all braces, conditions for a correct HTML code, then creates a 'parsed HTML'
        # we save this 'parsed HTML' to a variable and then navigate through it


# Navigation through HTML
    # HTML Once parsed, There are several ways to navigate:
        # By Tag Name
        # Using 'find()' - returns one matching tag
        # Using 'find_all' - returns a 'list' of matching tags



# ---------------    Navigating with CSS Selectors    ---------------
# select() - returns a list of elements matching a CSS selector




# Example 1 : Navigating using find() and find_all(). We use a MOCKED HTML
    # MOCKED HTML: for now we assume that this data is comming from a "request"

# from bs4 import BeautifulSoup
# import bs4

html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First HTML Page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special">This list item is special.</li>
        <li class="special">This list item is also special.</li> 
        <li>This list item is not special.</li>
    </ol>
    <div data-example="yes">bye</div>
</body>
</html>
"""

# =======    importing & parsing    =======
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')

print(soup)
print(type(soup))   # <class 'bs4.BeautifulSoup'>, it's not a string anymore

# print(soup.prettify())    # prints html



# =======    navigating    =======

# now we can navigate
print(soup.body)
print(soup.body.div)    # returns the first <div>


# using find():
print(soup.find("div")) # also returns the first <div>
print(soup.find("li")) # returns the first <li>
# these are not strings
d = soup.find("div")
print(type(d))    # <class 'bs4.element.Tag'>


# using find_all():
divs = soup.find_all("div")
print(divs)     # returns list of <div>s

lis = soup.find_all("li")
print(lis)     # returns list of <li>s


# selecting by attribute, id, class
# ids
print(soup.find(id = "first"))  # using "id"


# class = "special" won't work
# To find classes, use "class_" with 'find_all()'
print(soup.find_all(class_ = "special"))  # using "class"


# attribute: to find the attribute - 'key="value"'
    # we use 'attrs' with 'find_all()' using dictionary format {"key":"value"}
print(soup.find_all(attrs = {"data-example" : "yes"}))  # using "attribute"

dt = soup.find_all(attrs = {"data-example" : "yes"})
print(dt)




# ---------------    CSS style selector    ---------------
# use 'select()' #id for ids and ".class" for classes
# e.g #foo abnd .bar

# --------    select    --------

# 'select()' - returns a list of elements matching a CSS selector 
# -----    Selector Cheatsheet    -------
    # Select by id of foo: #foo
    # Select by class of bar: .bar
    # Select children: div > p
    # Select descendents (used a sapce in between): div p
from bs4 import BeautifulSoup
soup2 = BeautifulSoup(html_str, 'html.parser')

dt_2 = soup2.select("#first")
print(dt_2) # notice a list is returned

# we need to extract the element from that list
print(dt_2[0])

# class
dt_3 = soup2.select(".special")
print(dt_3) # notice a list is returned

# tags
dt_4 = soup2.select("div")
print(dt_4) # notice a list is returned

# attributes, need to enclose inside square braces
dt_5 = soup2.select("[data-example]")
print(dt_5) # notice a list is returned


#  following is a comparison between HTML and CSS selectors

# find an element with an id of 'foo' 
soup.find(id="foo")
soup.select("#foo")[0]

# find all elements with a class of 'bar'
# carefull "class" is a reserved word in Python 
soup.find_all(class_="bar")
soup.select(".bar")

# find all elements with a data
# attribute of "baz"
# using the general attrs kwarg
soup.find_all(attrs={"data-baz": True})     # notice attribut is inside {}
soup.select("[data-baz]")




# ------------------    Accessing Data in Elements    ------------------
# Extracting data from the CSS, HTML elements

    # get_text() - access the inner text in an element
    # 'name' - tag name "its not a function"
    # 'attrs' - dictionary of attributes "its not a function"
    # You can also access attribute values using brackets!

# Lets consider following string, since the "requested HTML" sent as a giant string
html_str_2 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta class = "no_text" charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First HTML Page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special super-special">This list item is special.</li>
        <li class="special">This list item is also special.</li> 
        <li>This list item is not special.</li>
    </ol>
    <div data-example="yes">bye</div>
</body>
</html>
"""

from bs4 import BeautifulSoup
soup3 = BeautifulSoup(html_str_2, 'html.parser')


# ------    getText()    ------
dt_a = soup3.select(".special")
el = dt_a[0]
print(el.get_text()) # 

el # <li class="special">This list item is special.</li>

# getting all elements
for le in dt_a:
    print(le.get_text())

# No ERR if there is no inner-text
print(soup3.select(".no_text")[0].getText())


# ------    name    ------
# getting all tag names
for le in dt_a:
    print(le.name)
# li
# li



# ------    attrs    ------
# getting all attributes
# since there is only "class attributes" used, it will return the list of class
    # in key-value pair
for le in dt_a:
    print(le.attrs)

# output:
# {'class': ['special', 'super-special']}
# {'class': ['special']}


# specify specific "attributes"
for le in dt_a:
    print(le.attrs['class'])

# ['special', 'super-special']
# ['special']


# ------    using []    ------
#  other way of selecting "attribute"
attr = soup3.find("h3")["data-example"]
print(attr)     # yes

# finding "id"s inside all div
dv_id = soup3.find("div")["id"]
print(dv_id)     # first

# getting all div attributes
dv_attr = soup3.find("div").attrs
print(dv_attr)     # {'id': 'first'}





# -----------    navigate relatively    -----------
# navigating between elements : "realative" to each other
# find a parrent of an "li" or 'parent of pararent', or next sibling or decendent etc

# so we'll be navigating around a selected object

# ------    via tags    ------
    # parent / parents 
    # contents
    # next_sibling / next_siblings

# ------    Via Searching    ------
    # find_parent / find_parents
    # find_next_sibling / find_next_siblings
    # find_previous_sibling / find_previous_siblings


html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First HTML Page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special">This list item is special.</li>
        <li class="special">This list item is also special.</li> 
        <li class = "super-special">This list item is not special.</li>
    </ol>
    <div data-example="yes">bye</div>
</body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')


# ------------------    via tags    ------------------

data = soup.body.contents   # returns a list
print(data)     # notice "newline character" "\n"
# the new lines appears after the end of each tags/HTML-elements

# so we need to use index to navigate between tags
data = soup.body.contents[0]   # using index to get tags
print(data) # prints a newline


data = soup.body.contents[1]  
print(data) 

data = soup.body.contents[1].contents   # accessing contents of selected tag
print(data)


# NEXT SIBLING
# accessing <ol> (the next sibling to currently selected div)
# data = soup.body.contents[1].next_sibling   # actually give new-line, instead use following
data = soup.body.contents[1].next_sibling.next_sibling
print(data)


# PARENTS
data = soup.find(class_="super-special").parent    
# we selected a <li>, then we get it paranet, which is <ol>
print(data)

data = soup.find(class_="super-special").parent.parent  # returns the whole <body>
print(data)




# ------------------    via searching    ------------------
    # find_parent / find_parents
    # find_next_sibling / find_next_siblings
    # find_previous_sibling / find_previous_siblings


html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First HTML Page</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special midpart">This list item is special.</li>
        <li class="special">This list item is also special.</li> 
        <li class = "super-special">This list item is not special.</li>
    </ol>
    <div data-example="yes">bye</div>
</body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')
# via search
data = soup.find(id="first").find_next_sibling()    
# It returns the <ol> tag, not the "new line"
    # NOTE: in previous section "next_sibling" (find by tags), returned new line,
    # Also notice: unlike "next_sibling", 'find_next_sibling()'  is a method 

# via tag
data = soup.find(id="first").next_sibling # returns "new line"

# we can also chain it
data = soup.find(id="first").find_next_sibling().find_next_sibling()    # <div data-example="yes">bye</div>



# find previous sibling
data = soup.select('[data-example]')[1].find_previous_sibling()   

# we can pass strings as an argument
data = soup.find(class_="midpart").find_next_sibling()    # by default it finds <li class="special">
# we can specify the class or tag name of the next sibling as below
data = soup.find(class_="midpart").find_next_sibling(class_ = "super-special")    # Now it finds <li class="super-special">


# find parent
data = soup.find(class_="midpart").find_parent()    # returns the <li>'s paraent, i.e. <ol>
# but we can specify any parent as an argument
data = soup.find(class_="midpart").find_parent("body")    # returns the whole body, which is also <li>'s paraen


# find more info using DOCUMENTATION, use help() on any item. for example  
help(data)


