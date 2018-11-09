def rotationCheck(s1,s2):
  if s1==s2: return 1
  l=len(s2)
  for c,i in enumerate(s2):
    temp=s2[c:l]+s2.strip(s2[c:l])
    if temp==s1: return 1 
  
s1='abcdaef'
s2='cdaefab'
#s2='efabcda'

if rotationCheck(s1,s2):
  print 'Rotation is ON'
else: 
  print 'Rotation is OFF'
