'''
Write a program to find the most common words in a text file
'''

a=input().split()
h=list(set(a))
l=0

for i in h:
	if h.count(i)>l:
		l=h.count(i)
print(l)

