'''
Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.
'''

a=input().strip()
x=0
y=0

for i in a:
    if i.islower():
        x+=1
    else:
        y+=1

print("lower = "+x)
print("upper = "+y)
