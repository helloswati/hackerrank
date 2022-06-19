1-
# Python program to explain os.getcwd() method		
# importing os module
import os
	
# Get the current working
# directory (CWD)
cwd = os.getcwd()
	
# Print the current working
# directory (CWD)
print("Current working directory:", cwd)

2-
# Python program to change the
# current working directory

import os

# Function to Get the current
# working directory
def current_path():
	print("Current working directory before")
	print(os.getcwd())
	print()


# Driver's code
# Printing CWD before
current_path()

# Changing the CWD
os.chdir('../')

# Printing CWD after
current_path()

## Creating a Directory
3- os.mkdir
   os.makedirs

import os 
listdie# (path,dir.name)


## Listing out Files and Directories with Python
4-
os.listdir('/home/swati/Documents') # (path)

5-
## Deleting Directory or Files using Python
os.remove('/home/swati/Documents') (path)

6- 
## os.rmdir() method in Python is used to remove or delete an empty directory
os.rmdir(path)

7-
## Commonly Used Functions
import os
print(os.name)
output : posix
	
8-
## os.error
import os
try:
	# If the file does not exist,
	# then it would throw an IOError
	filename = 'GFG.txt'
	f = open(filename, 'rU')
	text = f.read()
	f.close()

# Control jumps directly to here if
# any of the above lines throws IOError.	
except IOError:

	# print(os.error) will <class 'OSError'>
	print('Problem reading: ' + filename)
	
# In any case, the code then continues with
# the line after the try/except
