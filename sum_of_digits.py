n=int(input("Enter an integer number : "))
ans=0
while n!=0:
    digit=n%10
    ans=ans+digit
    n=n//10
print("Sum of the digits of the number entered by the user : ",ans)
