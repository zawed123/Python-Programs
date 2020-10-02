#this is a pogram to check whether the integer is palindromic or not
print("pogram to check whether the integer is palindromic or not")
aa=int(input("enter the number:"))
conv_str=str(aa)
bb=conv_str.split()
le=len(conv_str)-1
new_str=str()
for i in range(le,-1,-1):
     new_str+=conv_str[i]

if conv_str==new_str:
    print("yes, it is palindromic")

else:
    print("no, it is not palindromic")
