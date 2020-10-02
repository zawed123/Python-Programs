# https://www.facebook.com/jyotiprakash.nayak.372/posts/1837128093092133
# subscibed by Code House
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
