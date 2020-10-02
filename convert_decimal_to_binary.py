#this pogramm convret deciaml to bianry
def dectbin(aa):
 a=aa
 k=0
 l=[]
 i=0
 h=-1
 s=str()
 while a>0:
  if a%2==0:
    l.append(0)
    i=i+1
    a=a//2
    
  else:
    l.append(1)
    i=i+1
    a=a//2

 for i in reversed(l):
    j=str(i)
    s=s+j
 print("binary is :",s)
print("pogramm to create decimal to bianry")
aa=int(input('enter decimal num:'))
dectbin(aa)
