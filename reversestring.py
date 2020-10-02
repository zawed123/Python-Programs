str=input('enter')
index=len(str)

sum=[]

while index>0:
    sum+=str[index-1]
    index=index-1

print(sum)
