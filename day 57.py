'''
Create a function that returns the key with the maximum value in a dictionary
'''


dictt = {'1': 100, '2': 1292, '3': 88}  
  
# Getting the key with maximum value  
Key_max = max(zip(dictt.values(), dictt.keys()))[1]  
print("The key with the maximum value is: ", Key_max)  