# https://www.facebook.com/harhar.modi.1232/posts/706155836649246
# Subscribed by Code House

# Linear Search in python

def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1

arr = ['a','b','c','d','e','f','g','h','i']
x = 'a'

print("element found at index "+str(linearsearch(arr,x)))
