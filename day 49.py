'''
Create a program that implements the bubble sort algorithm
'''


n=int(input())
a=list(map(int,input().split())
print(a)

for i in range(n):
	for j in range(n-1):
		if(a[j]>a[j+1]):
			t=a[j]
			a[j]=a[j+1]
			a[j+1]=t
print(a)