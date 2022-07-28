# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "noon"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")



# palindrome

a = "wow"

b = reversed(a)

b == a[::-1]
