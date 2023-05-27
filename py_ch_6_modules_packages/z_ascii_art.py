
# Example 2: Use module "pyfiglet" to make an ASCII art and then colorize it using "termcolor"

# pip install pyfiglet

# To get the ANSI codes working on windows, first run "os.system('color')"
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
# To get the ANSI codes working on windows, first run "os.system('color')"
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


''' 
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

cprint("Attention!", "red", attrs=["bold", "blink"], file=sys.stderr) '''

# python ascii_art.py