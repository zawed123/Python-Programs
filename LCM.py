# https://www.facebook.com/100025945953774/posts/695502641324595/?app=fbl
# subscribed by code house
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))
