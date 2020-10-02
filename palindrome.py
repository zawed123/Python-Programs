
# https://www.facebook.com/permalink.php?story_fbid=2830418890577388&id=100008279138695
# Subscribed by Code House

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
"""
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
"""
