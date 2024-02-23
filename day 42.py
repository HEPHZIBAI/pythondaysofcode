'''
Write a program that uses a try-except block to handle division by zero
'''

try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

    print(result)
except ValueError as e:
    print("Invalid Input Please Input Integer...")
except ZeroDivisionError as e:
    print(e)