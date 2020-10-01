# https://www.facebook.com/jasmeet.singh.77920/posts/3180825812045692
# Subscribed by Code House

num = 407

#num = int(input("Enter a number: "))

if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
