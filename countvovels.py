s=input('enter str')
s=s.lower()

count=0
list=['a','e','i','o','u']

for i in s:
    if i in list:
        count=count+1
print(count)
