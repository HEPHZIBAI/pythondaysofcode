'''
Write a function that takes a list of numbers and returns a new list containing only the even numbers.
'''
a=list(map(int,input().split()))
for i in a:
	if i%2!=0:
		a.remove(i)
	

