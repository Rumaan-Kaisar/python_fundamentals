# Courses: colt_py_bootcamps 50  

# ------------ Escape Seqences --------------
# Code	    Result
\'	        Single Quote	
\\	        Backslash	
\n	        New Line	
\r	        Carriage Return	
\t	        Tab	
\b	        Backspace	
\f	        Form Feed	
\ooo	    Octal value	
\xhh	    Hex value

str_1 = "Hi!\nThere\nwhat is 10/9 = \\"
print(str_1)

# using backslash
str_2 = "Whats My na\bme?"
print(str_2)

# using double-quote inside double-quote, or single-quote inside singele/double-quote
heavy_quotation = "Whats My \"na\bme\", its \'crazy\' right?"
print(heavy_quotation)
