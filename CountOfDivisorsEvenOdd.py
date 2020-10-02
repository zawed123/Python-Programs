#DarkSouL

# Python program to find if count of divisors is even or odd.

def NumOfDivisor(n):
	if n < 1:
		return
	root_n = n**0.5
	if root_n**2 == n:
		print("Odd")
	else:
		print("Even")
if __name__ == '__main__':
    print("Enter a number : ", end=" ")
    n = int(input())
    print("The count of divisors of", n, "is:", end=" ")
    NumOfDivisor(n)
