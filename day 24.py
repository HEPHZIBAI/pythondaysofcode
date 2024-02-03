'''
Write a program to remove vowels from a given string.
'''
a=input().strip()
b=""
for i in a:
	if i not in "aeiouAEIOU":
		b+=i
print(b)