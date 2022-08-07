# Program to print full pyramid 
num_rows = int(input("Enter the number of rows"));
for i in range(0, num_rows):
	for j in range(0, num_rows-i-1):
		print(end=" ")
	for j in  range(0, i+1):
		print("*", end=" ")
	print()


2.
#Program to print Left Half Pyramid
num_rows = int(input("Enter the number of rows"));
k = 1
for i in range(0, num_rows):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()

3. 
