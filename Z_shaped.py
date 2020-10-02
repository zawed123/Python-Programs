
# https://www.facebook.com/sandeepmore.more.5/posts/1261804104181092
# subscribed by code House

for i in range(1,6):
    for j in range(1,6):
        # i=1 for top line 
        # i=5 for bottom line
        # (i+j)=6 for diagonal
        if i==1 or i==5 or (i+j)==6:
            print("*",end=" ")
            else:
                print(" ",end="")
    
            print("")
