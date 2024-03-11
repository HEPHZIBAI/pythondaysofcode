'''
Create a function that takes a string and returns the reverse of each word
'''

a=input().split()

b=""

for i in a:
	b+=i[::-1]+" "
return b