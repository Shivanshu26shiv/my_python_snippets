'''
Purpose: To remove duplicates from a string in a short way
By: Shivanshu
'''

s='geeks for geeks'
l=[]
map(lambda x: l.append(x) if x not in l else None,s)
print ''.join(l)

