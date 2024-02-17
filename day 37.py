'''
Write a program to iterate through a dictionary and print its keys and values
'''

a={1:'a',2:'b',3:'c'}
v=list(a.keys())
for i in v:
	print(i,a[i])
