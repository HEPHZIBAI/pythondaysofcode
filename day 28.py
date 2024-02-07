'''
Create a program that removes the nth element from a list.
'''

a=list(map(int,input().split()))
n=int(input())
del a[n]
print(a)