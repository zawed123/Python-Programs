#https://www.facebook.com/ratnadeep.pragwalit/posts/2791088471172809
#Subscribed by Ratnadeep Ghosh

s=input()
m=0
        
s1=""
j=0
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[j] not in s1:
            s1=s1+s[j]
        else:
            break
    m=max(m,len(s1))  
    s1=""
                    
print(m) 
