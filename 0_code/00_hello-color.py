'''
The goal is to use the termcolor package to print "Hello World".
'''

from termcolor import colored

'''
termcolor: https://pypi.org/project/termcolor/

Colors: grey, red, green, yellow, blue, magenta, cyan, 
		and white
Highlights: on_grey, on_red, on_green, on_yellow, on_blue,
		on_magenta, on_cyan, and on_white
Attributes: blod, dark, underline, blink, reverse, 
		and concealed
'''
print(colored(
	'This file uses the termcolor package to print "Hello World" in flashing colors.', 
	'blue', 'on_yellow', 
	attrs = ['bold','underline']))

print(colored(
	'<3<3<3<3<3<3', "grey" , 'on_magenta', 
	attrs =['bold','reverse']
	))

print(colored(
	'Hello, World!', 'magenta', 
	attrs = ['bold','blink']
	))

print(colored(
	'Hello, World!', 'magenta', 
	attrs =['bold','reverse', 'blink']
	))

print(colored(
	'<3<3<3<3<3<3', 'magenta', 
	attrs = ['bold']
	))