
# Courses: colt_py_bootcamps    220, 221

# Example 1: Use termcolor to colorize your text

# pip install termcolor

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




# Example 2: Use module "pyfiglet" to make an ASCII art and then colorize it using "termcolor"

# pip install pyfiglet
import termcolor
import pyfiglet

# help(termcolor)

ask_msg = input("What message do you want to print : ")
ask_clor = input("What Color : ")

# help(termcolor) # use it to get availabe colors list

''' Available text colors:
            black, red, green, yellow, blue, magenta, cyan, white,
            light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
            light_magenta, light_cyan. '''

asci_art = pyfiglet.figlet_format(ask_msg)

term_color_list = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
            "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue",
            "light_magenta", "light_cyan"]

print(asci_art)

if ask_clor in term_color_list:
    print(termcolor.colored(asci_art, color=ask_clor))
else:
    print(termcolor.colored(asci_art, color = term_color_list[2]))



# -------------- another way ------------
''' 
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
