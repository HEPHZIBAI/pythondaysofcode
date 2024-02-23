'''
Write a program that uses recursion to generate all permutations of a list
'''


  
def toString(List): 
    return ''.join(List) 
  
def permute(a, l, r): 
    if l == r: 
        print(toString(a)) 
    else: 
        for i in range(l, r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]  # backtrack 
  
  
string = "ABC"
n = len(string) 
a = list(string) 
  
permute(a, 0, n) 