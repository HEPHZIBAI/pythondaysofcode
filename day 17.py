'''
Create a program that capitalizes the first letter of each word in a sentence
'''

a=input().split()
for i in a:
	print(i.title(),end=" ")