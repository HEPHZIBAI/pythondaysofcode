'''
Write a function to check if a given list is sorted
'''

a=list(map(int,input().split()))
b=a
b.sort()
if a==b:
	print("yes")
else:
	print("no")