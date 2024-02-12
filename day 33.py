'''
Write a test case for a function that checks if a number is prime
'''

def prime(a):
	for i in range(2,a):
		if a%i==0:
			return False
	return True