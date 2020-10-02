# https://www.facebook.com/tanishka.gupta.52090/posts/687845045495680
# Subscribed by Tanishka Gupta


def compute_lcm(x, y):

  
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
