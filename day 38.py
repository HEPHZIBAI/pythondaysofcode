'''
Write a program to flatten a nested list
'''
 
def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList
 
 
lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
print('List', lis)
print('Flat List', flat(lis))