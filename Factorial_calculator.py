#https://www.facebook.com/100051921408118/posts/190716086002437/?app=fbl
#Subscribed by CodeHouse
inp=int(input("Enter the number : "))

def f(n):

	fac=1

	for i in range(n):

		fac=fac*(i+1)

	return fac

print("Factoial is ",f(inp))
