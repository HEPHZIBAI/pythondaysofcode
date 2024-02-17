'''
Write a Python program to merge two dictionaries
'''
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of the first dictionary to avoid modifying it
    merged_dict.update(dict2)   # Update the copy with the contents of the second dictionary
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3=dict1.copy()
dict3.update(dict2)
