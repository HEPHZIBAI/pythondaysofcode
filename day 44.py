'''
Write a program that reads an integer from the user and handles invalid inputs
'''
try: 
	num = int(input("Enter an integer: ")) 
	print("The entered number is:", num) 
except ValueError: 
	print("Invalid input. Please enter an integer)
