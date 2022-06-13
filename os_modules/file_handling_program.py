1- Write a Program to create a file -> main.txt 
Solution : 
# create a empty text file
# in current directory
import os
fp = open('main.txt', 'x')
fp.close()

2- Create a folder ->  demo 
Solution:
# Python program to explain os.mkdir() method
# importing os module
import os
# Create the directory
#'/home / User / Documents'
os.mkdir('/home/swati/Documents/demo')

3- Create a file in the demo folder
Solution:
import os
os.makedirs('/home/swati/Documents/demo/main.txt')

4- List all files in a directory 
Solution:
import os
path = "/"
dir_list = os.listdir('/home/swati/Documents/demo')
print(dir_list)
Output: main.txt
  
