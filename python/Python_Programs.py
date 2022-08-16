12

n = 2

1  2 
 
1 4 = 6

153

n = 3

1 5 3 = 1 + 125 + 27 = 153 armstrong 

F3=F2+F1 
  =1+0 
  =1 
F4=F3+F2 
  =1+1 
  =2 
  0 1 1 2 3 5 8 13 21 29 37 fibonacci

n = 153 # or n=int(input()) 
s = n 
b = len(str(n))
sum1 = 0
while n != 0:
	r = n % 10
	sum1 = sum1+(r**b)
	n = n//10
if s == sum1:
	print("The given number", s, "is armstrong number")
else:
	print("The given number", s, "is not armstrong number")




# palindrome
def isPalindrome(s):
	return s == s[::-1]

s = "noon"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")


# fibonacci

def fibonacci(N):
    if N == 1:
        return 0
    if N == 2:
        return 1
    return fibonacci(N - 1) + fibonacci(N - 2)


print("3rd term of the fibonacci series is:")
print(fibonacci(3))



# calculator 

def add(a,b):
     return a+b
 
def sub(a,b):
     return a-b
 
def multiply(a,b):
     return a * b
 
def div(a,b):
     return a / b

print(multiply(10,15))
print(add(50,50))


#Program to print Left Half Pyramid

num_rows = int(input("Enter the number of rows"));
k = 1
for i in range(0, num_rows):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()

# Reverse a list / string 

a = [1,2,3,4,5,6,7,8,9,10]
print(a[: : -1])
#this will print the list in reverse.


# factorial

def fact(num):
    if num == 0:
       return num
    else:
       return num * fact(num - 1)
print(fact(5))