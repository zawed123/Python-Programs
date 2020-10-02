#this pogramm convret binary to deciaml
def bintdec(aa):
 aa=str(aa)
 a=[]
 for x in aa:
    x=int(x)
    a.append(x)

 l=len(a)
 c=l-1
 dec=0
 for i in a:
    dec=dec+(i*2**c)
    
    c=c-1
    
 print("decimal is :",dec)

print("pogramm to create binary to decimal")
aa=int(input('enter binary num:'))
bintdec(aa)
