1- Write a Program to create a file -> main.txt 
Solution : 
# create a empty text file
# in current directory
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
