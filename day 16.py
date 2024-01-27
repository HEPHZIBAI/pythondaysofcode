'''
Write a function that counts the frequency of each word in a sentence.
'''
a=input().split()
b=set(a)
for i in b:
	print(i,a.count(i))