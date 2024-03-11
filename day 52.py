'''
Create a program that checks if a string is a palindrome
'''


a=input().strip()
if a==a[::-1]:
	print("palindrome")
else:
	print("not a apalindrome")