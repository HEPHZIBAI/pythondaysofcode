'''
Write a function to find the largest common divisor of two numbers using a function
'''

def gcd(a, b):
 
    # Find minimum of a and b
    result = min(a, b)
 
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
 
    # Return the gcd of a and b
    return result