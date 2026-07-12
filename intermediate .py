Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']


'''
new_names = []
for n in Names:
    new_names.append(n.upper())

print(list(new_names))
'''


'''
def uppercase (n):
    return n.upper()

new_names = map(uppercase , Names)

print(list(new_names))
'''


'''
new_names = [n.upper() for n in Names]
print(new_names)

'''

'''
new_names = []
for n in Names:
    if 'a'in n:
        new_names.append(n)

print(list(new_names))    
'''

'''
def Search(n):
    if 'a' in n:
     return n 
new_names = map(Search,Names)
print(list(new_names))
'''

'''
new_names = [ n for n in Names if 'a' in n ]

print(new_names)
'''

'''

new_names = []
for n in Names:
    if n.startswith('t'):
        new_names.append(n)

print(list(new_names))
'''

'''
def Startwith (n):
    if n.startswith('t'):
        return n
    
        

new_names = filter(Startwith , Names)
print(list(new_names))
'''

'''

new_names = [ n for n in Names if n.startswith('t') ]
print(new_names)
'''

'''
new_names = []

for n in Names:
    if n.count('a') >= 2:
        new_names.append(n)

print(new_names)
'''


'''

def Count(n):
    if n.count('a') >=2:
        return n
    

new_names = filter(Count , Names)
print(list(new_names))
'''


new_names = [n for n in Names if n.count('a')>= 2 ]
print(new_names)
















