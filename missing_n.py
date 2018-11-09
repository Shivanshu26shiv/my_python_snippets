
s='geeks for geeks'
l=[]
'''
for i in s:
    if i not in l:  l.append(i)
        
print ''.join(l)
'''

map(lambda x: l.append(x) if x not in l else None,s)
print ''.join(l)

#print map(lambda x: True if x % 2 == 0 else False, range(1, 11))
