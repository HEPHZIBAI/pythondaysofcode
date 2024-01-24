'''
Write a program to print the first n numbers of a Fibonacci sequence
'''

n=int(input())
if n==1:
	print(0)
elif n==2:
	print('0 1')
else:
	a=0
	b=1
	c=a+b
	print(a,b,c,sep=" ",end=" ")
	for i in range(3,n+1):
		a=b
		b=c
		c=a+b
		print(c,end=" ") 