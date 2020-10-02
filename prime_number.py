num=int(input("Enter a number : "))
x=False
for i in range(2,num):
    if num%i==0:
        x=True
        break
if x==True:
    print("Number is not prime")
else:
    print("Number is Prime")