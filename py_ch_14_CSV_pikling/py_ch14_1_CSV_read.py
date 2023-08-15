
# Courses: colt_py_bootcamps    314

# ---------------    CSV    ---------------
# CSV: comma seperated values
    # its a common format to represent/store data
    # It works withh homogenous data that follows a pattern

# Following is a demo of a CSV file: 'fighter.csv'
""" 
Name,Country,Height (in cm) 
Ryu,Japan,175 
Ken,USA,175 
Chun-Li,China,165 
Guile,USA,182 
E. Honda,Japan,185 
Dhalsim,India,176 
Blanka,Brazil,192 
Zangief,Russia,214
"""


# Reading CSV Files;
    # CSV files are a common file format for tabular data 
    # read(): We can read CSV files just like other text files 
    # CSV module: Python has a built-in 'CSV' module to read/write CSVs more easily



# Example 1: read a csv file using read()
with open('fighters.csv') as fiL:
    fiL.read()

# We'll get a giant string as below
'Name,Country,Height (in cm) \nRyu,Japan,175 \nKen,USA,175 \nChun-Li,China,165 \nGuile,USA,182 \nE. Honda,Japan,185 \nDhalsim,India,176 \nBlanka,Brazil,192 \nZangief,Russia,214'


# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!
with open("fighters.csv") as file:
    data = file.read()




# --------------    CSV module    --------------
# There is two different ways to read using CSV module
    # reader: returns each 'row' as a 'list'
        # lets you iterate over rows of the CSV as lists DictReader

    # dictReader: Returned as an Ordered Dictionery
        # lets you iterate over rows of the CSV as OrderedDicts
        # Keys are determined by the header row


# using reader:
# it reaurns an "_csv.reader" object, which is an 'ITERATOR' and RUNS ONLY ONCE
from csv import reader 

with open("fighters.csv") as file:
    # apply "reader" 
    csv_reader = reader(file)   # reader() returns an "iterator" not a "list"
    for row in csv_reader:      # RUNS ONLY ONCE
        # each row is a list 
        print(row)

"""  
    ['Name', 'Country', 'Height (in cm) ']
    ['Ryu', 'Japan', '175 ']
    ['Ken', 'USA', '175 ']
    ['Chun-Li', 'China', '165 ']
    ['Guile', 'USA', '182 ']
    ['E. Honda', 'Japan', '185 ']
    ['Dhalsim', 'India', '176 ']
    ['Blanka', 'Brazil', '192 ']
    ['Zangief', 'Russia', '214']
"""



# using DictReader:
# DictReader() also returns an "iterator"
    # Benifit: We dont need to think about "HEADER"
from csv import DictReader 

with open("fighters.csv") as file: 
    # apply "DictReader" 
    csv_reader = DictReader(file)       # DictReader() also returns an "iterator"
    for row in csv_reader:          # RUNS ONLY ONCE
        # each row is an OrderedDict !
        print(row)

"""  
    {'Name': 'Ryu', 'Country': 'Japan', 'Height (in cm) ': '175 '}
    {'Name': 'Ken', 'Country': 'USA', 'Height (in cm) ': '175 '}
    {'Name': 'Chun-Li', 'Country': 'China', 'Height (in cm) ': '165 '}
    {'Name': 'Guile', 'Country': 'USA', 'Height (in cm) ': '182 '}
    {'Name': 'E. Honda', 'Country': 'Japan', 'Height (in cm) ': '185 '}
    {'Name': 'Dhalsim', 'Country': 'India', 'Height (in cm) ': '176 '}
    {'Name': 'Blanka', 'Country': 'Brazil', 'Height (in cm) ': '192 '}
    {'Name': 'Zangief', 'Country': 'Russia', 'Height (in cm) ': '214'}
"""




# Example 1: Using reader
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) #To skip the headers
    for fighter in csv_reader:
    	# Each row is a list
    	# Use index to access data
    	print(f"{fighter[0]} is from {fighter[1]}") 




# Example 2: where data is cast into a list
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)




# Example 3: Reading/Parsing CSV Using a DictReader:
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name']) #Use keys to access data





# --------------    Other Delimiters    --------------
# Seperators other than ',', e.g. '|' or '$'
    # reader() accept a "delimiter" kwarg in case your data isn't separated by commas.



# Example 4: working with seperator other tahn ','
from csv import reader

with open("example.csv") as file:
    csv_reader = reader(file, delimiter="|") 
    for row in csv_reader:
        # each row is a list! 
        print(row)
