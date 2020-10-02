# https://www.facebook.com/tanishka.gupta.52090/posts/687845045495680
# Subscribed by Tanishka Gupta

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')


dec = 34

convertToBinary(dec)
print()
