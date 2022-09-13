'''
The goal is to ask the user for two numbers and an 
arithmetic (addition, subtraction, multiplication, or division).
Then the program prints the solution of the operation on 
the two numbers that were given. 
'''

from termcolor import colored

# text greeting and instructions to user
instructions = '''
Hello User!
This file will ask for two integers and an arithmetic operation 
(addition, subtraction, multiplication, or division) then preform 
that operation on the two numbers given.'''

# prints instructions
print(colored(
	instructions, 
	'blue', 'on_yellow', 
	attrs = ['bold']))

# Request Input
print("Please enter an integer and press enter.")

# First Input
num1 = int(input())

# Request second input
print("Please enter a second integer and press enter.")
num2 = int(input())

# Request operation 
print("Please enter an operation: addition, subtraction, multiplication, or division")
operation =  str(input())

# sorts input and applies appropriate solution and op
if operation == "addition":
	solution = num1 + num2
	op = "+"
elif operation == "subtraction":
	solution = num1 - num2
	op = "-"
elif operation == "multiplication":
	solution = num1 * num2
	op = "*"
elif operation == "division":
	solution = num1 / num2
	op = "/"
else:
	solution = "not valid, try again"
	op = "?"

# printing the sum in integer
print(num1 ,op , num2, "is", solution, ".")