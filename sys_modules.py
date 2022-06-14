# The sys module in Python provides various functions and variables that are used to 
# to manipulate different parts of the Python runtime environment
1-
import sys
  
print(sys.version)

2-
# stdin

import sys
for line in sys.stdin:
	if 'q' == line.rstrip():
		break
	print(f'Input : {line}')

print("Exit")

3-
# stdout

import sys
sys.stdout.write('Geeks')

4-
# stderr

import sys

def print_to_stderr(*a):

	# Here a is the array holding the objects
	# passed as the argument of the function
	print(*a, file = sys.stderr)

print_to_stderr("Hello World")

5-
## Command Line Arguments
# It is a list of command-line arguments.
# len(sys.argv) provides the number of command-line arguments.
# sys.argv[0] is the name of the current Python script.

# sys.argv
# Python program to demonstrate
# command line arguments

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
	print(sys.argv[i], end = " ")
	
# Addition of numbers
Sum = 0

for i in range(1, n):
	Sum += int(sys.argv[i])
	
print("\n\nResult:", Sum)

7-
# Exiting the Program
## sys.exit([arg])

# Python program to demonstrate
# sys.exit()

import sys

age = 17

if age < 18:
	
	# exits the program
	sys.exit("Age less than 18")	
else:
	print("Age is not less than 18")


8-
# Working with Modules
## sys.path is an ordinary list and can be manipulated.

import sys
print(sys.path)

# Truncating the value of sys.path

import sys

# Removing the values
sys.path = []

# importing pandas after removing
# values
import pandas

9-
# sys.modules return the name of the Python modules that the current shell has imported.

import sys

print(sys.modules)

10-
# Reference Count
## sys.getrefcount() 

import sys

a = 'Geeks'

print(sys.getrefcount(a))





