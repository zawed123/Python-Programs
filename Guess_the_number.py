#https://www.facebook.com/100051921408118/posts/190716086002437/?app=fbl
#Subscribed by CodeHouse
print("Welcome to the guess the number game\n")

print("You have to guess the number\n")

print("Hint : The number is between 1-50\n")

import random

num=random.randint(1,50)

a=7

while a>0:

	guess=int(input("Enter your guessed number : "))	if guess==num:

		print("You won!")

		break

	

	elif guess>num:

		print("Too high")

		a=a-1

		print("You are left with ",a,"guesses\n")

		continue

		

	elif guess<num:

		print("Too low")

		a=a-1

		print("You are left with ",a,"guesses\n")

		continue

if a==0:

	print("You lose! Better luck next time")

	
