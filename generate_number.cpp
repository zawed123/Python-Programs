# https://www.facebook.com/nitesh.kushwaha.399488/posts/2679421279041581
# subsribed by Happy Kumar


# this program generates a random number of given d digits
import random
d=int(input('enter number of digits'))
n=0
for i in range(0,d):
    x=int(random.random())%10
    if(i==0 and x==0):
        x=1
    n=(n*10)+x 
print(n)
