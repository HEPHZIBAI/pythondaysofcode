'''
Create a function to find all words in a sentence that start with a vowel
'''
a=input().split()

for i in a:
	if i[0] in "aeiouAEIOU":
		print(i)