#subscribed code house and shared
n=int(input("ENTER TO REVERSE"))
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)
