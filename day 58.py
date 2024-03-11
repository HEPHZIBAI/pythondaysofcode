'''
Create a function that converts a string to an integer and handles ValueError
'''

user_input  =  input("Enter a number: ")
try:
	number  =  int(user_input)
	print("Converted integer:", number)
except  ValueError:
	print("Invalid input. Please enter a valid number.")