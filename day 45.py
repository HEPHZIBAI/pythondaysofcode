'''
Write a function to check if a number is a prime number
'''

n=int(input())
f=1
for i in range(2,n):
	if n%i==0:
		f=0
		break
if f==1:
	print("prime number")
else:
	print("not a prime number")