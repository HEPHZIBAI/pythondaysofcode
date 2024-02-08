'''
Create a function that generates a random number between a given range.
'''

import random 
x=int(input("start : "))
y=int(input("end : "))
n = random.randint(x,y) 
print(n)