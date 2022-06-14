import os

# Function to Get the current 
# working directory
def current_path():
    print(os.getcwd())


# Print current working directory
print ("Current Working Directory is ", os.getcwd())



# Changing the CWD
os.chdir('../')
   
# Printing CWD after
print ("Current Working Directory is ", os.getcwd())



