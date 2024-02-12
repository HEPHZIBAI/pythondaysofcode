'''
Create a function that finds the second smallest element in a list.
'''
a=list(map(int,input().split()))
b=a
b.sort(reverse="True")
print(b[1])