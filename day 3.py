'''Write a function to count the number of vowels in a given string '''

a=input().strip()
c=0
for i in a:
	if i in "aeiouAEIOU":
		c+=1
print(c)
