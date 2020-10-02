#pogramm to fin lcm and hcf
print("pogramm to check lcm and hcf")
a=int(input("enter first number:"))
b=int(input("enter second number:"))
k=[]
m=[]
l=[]
for i in range (1,a+1):
    if a%i==0:
        k.append(i)

for n in range (1,b+1):
    if b%n==0:
        m.append(n)

for g in k:
    for lg in m:
        if g==lg:
            l.append(g)
l.sort()

hcf=l[-1]
#print (l,hcf)
print("HCF of",a,"and",b,":",hcf)

num1=a//hcf
num2=b//hcf
lcm=hcf*num1*num2
print("LCM of",a,"and",b,":",lcm)
