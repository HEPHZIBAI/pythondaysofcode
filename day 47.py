'''
Create a program that imports the math module and uses its functions
'''
import math  
n=int(input("enter a nmber :"))
print("ceil value ",math.ceil(n))
print("floor value" ,math.floor(n))
n=int(input("enter a number to find its factorial :"))  
print("factorial of ",n," is ",math.factorial(n))  
print("square root of ",n,"is ",math.sqrt( n )) 
exp=int(input("enter the exponent value"))  
res=math.pow(num, exp)  
print(n," power ",exp," is ",res)
print("enter two number to find its gcd")
n1=int(input("n1: "))  
n2=int(input("n2: "))  
res=math.gcd(n1,n2)  
print("gcd of ",n1," and ",n2," is ",res)    
print("pi value is ",math.pi)  





  