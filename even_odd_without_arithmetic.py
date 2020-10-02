#Program to check wheather number is even or odd without using arithmatic operators:
n=int(input("enter the number: "))
if n & 1 ==0 :
	print("The number is even")
else:
	print("The number is odd")