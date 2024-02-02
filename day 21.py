'''
Create a program to remove a specific element from a set.
'''
a=set(map(int,input().split()))
n=int(input())

a.remove(n)
print(a)