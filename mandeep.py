n =int(input("Enter Number: "))
sum=0
t=n
while t>0:
   d =t%10
   s+=d**3
   t//=10
if n==sum:
  print("Armstrong Number")
 else:
  print("Not Armstrong Number")
