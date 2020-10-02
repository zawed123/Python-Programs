# https://www.facebook.com/harhar.modi.1232/posts/706155836649246
# Subscribed by Code House
# Fibonacci Series Program using recursion in python


def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
print(Fibonacci(9))
