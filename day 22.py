'''
Create a program to find the second-largest element in a list.
'''
a=list(map(int,input().split()))
a.sort(reverse=True)
print("second largest",a[1])