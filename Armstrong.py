# https://www.facebook.com/permalink.php?story_fbid=1284725128547130&id=100010289646874
# Subscribed by ARS Army
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320

print_factors(num)
