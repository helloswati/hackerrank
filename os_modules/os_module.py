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
os.mkdir('/home/swati/Documents',"Geeks")  # (path,dir.name)


## Listing out Files and Directories with Python
4-
os.listdir('/home/swati/Documents') # (path)

