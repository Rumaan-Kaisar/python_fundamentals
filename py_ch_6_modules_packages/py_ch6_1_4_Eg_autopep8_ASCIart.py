
# Courses: colt_py_bootcamps    220, 221, 222


# ---------------    termcolor    ---------------
# In WINDOWS CLI, 'ANSI color codes' won't work at first
	# To get the 'ANSI codes' working on WINDOWS, first run "os.system('color')"
import os	
os.system('color')



# termcolor usage demo
import os, sys

# To get the ANSI codes working on windows, first run
os.system('color')

from termcolor import colored, cprint

text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
    cprint(i, "magenta", end=" ")

cprint("Attention!", "red", attrs=["bold", "blink"], file=sys.stderr)




# Example 1: Use 'termcolor' to colorize your text

# pip install termcolor

# To get the 'ANSI codes' working on WINDOWS, first run "os.system('color')"
import os	
os.system('color')

import termcolor
help(termcolor) # won't work if not imported the module first

''' Help on package termcolor:

NAME
    termcolor - ANSI color formatting for output in terminal.

PACKAGE CONTENTS
    __main__
    termcolor

FUNCTIONS
    colored(text: 'str', color: 'str | None' = None, on_color: 'str | None' = None, attrs: 'Iterable[str] | None' = None) -> 'str'
        Colorize text.

        Available text colors:
            black, red, green, yellow, blue, magenta, cyan, white,
            light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
            light_magenta, light_cyan.

        Available text highlights:
            on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
            on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
            on_light_blue, on_light_magenta, on_light_cyan.

        Available attributes:
            bold, dark, underline, blink, reverse, concealed.

        Example:
            colored('Hello, World!', 'red', 'on_black', ['bold', 'blink'])
-- More  -- '''

print(dir(termcolor))


# The coloring is done with "ASCII color-codes"

# Bacground color change
clr_txt = termcolor.colored("OMG!!", color="red", on_color="on_cyan")
print(clr_txt)

# adding attributes: bold, dark, underline, blink, reverse, concealed
clr_txt = termcolor.colored("OMG!!", color="red", on_color="on_cyan", attrs=["bold", "blink"])
print(clr_txt)


# We can import only "colored"
from termcolor import colored

text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)




# Example 2: Use module "pyfiglet" to make an 'ASCII art' and then colorize it using "termcolor"

# pip install pyfiglet

# To get the 'ANSI color codes' working on WINDOWS, first run "os.system('color')"
import os	
os.system('color')

import termcolor
import pyfiglet

ask_msg = input("What message do you want to print : ")
ask_clor = input("What Color : ")
ask_bg_clor = input("On what Background Color : ")


# help(termcolor) # use it to get availabe colors list

''' Available text colors:
            black, red, green, yellow, blue, magenta, cyan, white,
            light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
            light_magenta, light_cyan. '''

asci_art = pyfiglet.figlet_format(ask_msg)

term_color_list = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
            "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue",
            "light_magenta", "light_cyan"]

# bacground: just add "on_"+term_color_list[i]

if (ask_clor in term_color_list):
    if (ask_bg_clor in term_color_list):
        bcgnd = "on_"+ask_bg_clor
        print(termcolor.colored(asci_art, color=ask_clor, on_color= bcgnd))
    else:
        print(termcolor.colored(asci_art, color=ask_clor))
else:
    print(termcolor.colored(asci_art, color = "light_green"))


''' 
# -------------- another way ------------
# To get the 'ANSI color codes' working on windows, first run "os.system('color')"
import os	
os.system('color')

from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	if color not in valid_colors:
		color = "magenta"

	ascii_art = figlet_format(msg)
	colored_ascii = colored(ascii_art, color=color)
	print(colored_ascii)

msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)

'''

# python py_ch6_1_4_Eg_autopep8_ASCIart.py





# ---------------    autopep8 : to cleanup codes    ---------------

# always KEEP BACKUP OF YOUR ORIGINAL FILE before applying autopep8

# pip install autopep8

''' autopep8 automatically formats Python code to conform to the PEP 8 style guide. 
It uses the pycodestyle utility to determine what parts of the code needs to be formatted. 
autopep8 is capable of fixing most of the formatting issues that can be reported by pycodestyle. '''

# Before running autopep8.

import math, sys;

def example1():
    ####This is a long comment. This should be wrapped to fit within 72 characters.
    some_tuple=(   1,2, 3,'a'  );
    some_variable={'long':'Long code lines should be wrapped within 79 characters.',
    'other':[math.pi, 100,200,300,9876543210,'This is a long string that goes on'],
    'more':{'inner':'This whole logical line should be wrapped.',some_tuple:[1,
    20,300,40000,500000000,60000000000000000]}}
    return (some_tuple, some_variable)
def example2(): return {'has_key() is deprecated':True}.has_key({'f':2}.has_key(''));
class Example3(   object ):
    def __init__    ( self, bar ):
     #Comments should have a space after the hash.
     if bar : bar+=1;  bar=bar* bar   ; return bar
     else:
                    some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
                    return (sys.path, some_string)



# AGGRESSIVE LEVEL
# To modify a file in place (with aggressive level 2):

autopep8 --in-place --aggressive --aggressive <filename>


# After running autopep8: After running the above command in CLI:
import math
import sys


def example1():
    # This is a long comment. This should be wrapped to fit within 72
    # characters.
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        'long': 'Long code lines should be wrapped within 79 characters.',
        'other': [
            math.pi,
            100,
            200,
            300,
            9876543210,
            'This is a long string that goes on'],
        'more': {
            'inner': 'This whole logical line should be wrapped.',
            some_tuple: [
                1,
                20,
                300,
                40000,
                500000000,
                60000000000000000]}}
    return (some_tuple, some_variable)


def example2(): return {'has_key() is deprecated': True}.has_key(
    {'f': 2}.has_key(''))


class Example3(object):
    def __init__(self, bar):
        # Comments should have a space after the hash.
        if bar:
            bar += 1
            bar = bar * bar
            return bar
        else:
            some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
            return (sys.path, some_string)


