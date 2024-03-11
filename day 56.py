'''
Create a function to extract all URLs from a given text using regular expressions
'''


import re
 
with open("path\url_example.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls)