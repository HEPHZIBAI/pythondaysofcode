'''
Write a Python program to check if two strings are anagrams
'''
a=input().strip()
b=input().strip()

d=list(set(a))
m=1

for i in d:
	if a.count(i)!=b.count(i):
		m=0
		break
if m==1:
	print("yes")
else:
	print("no")