'''
Create a function that checks if a number is a perfect square
'''

import math  
num = 25  
sqrt_num = math.sqrt(num)  
if sqrt_num.is_integer():  
    print("The number is a perfect square")  
else:  
    print("The number is not a perfect square")  