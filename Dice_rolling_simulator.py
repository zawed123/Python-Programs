#https://www.facebook.com/100051921408118/posts/190716086002437/?app=fbl
#Subscribed by CodeHouse
import random

import time

print("----------Welcome to 'Roll the dice'-----------")

dice=input("Do you want to roll the dice?(y/n)\n")

if dice=="y":

	while dice=="y":

		num=random.randint(1,6)

		print("Dice is rolling...")

		time.sleep(2)

		print(f"And the number is...{num}\n\n")

		time.sleep(1)

		

		dice=input("Do you want to roll the dice again?(y/n) ")

		

		if dice=="n":

			print("Thanks for using this Dice Roll Simulator")

		

elif dice=='n':

	print("Thanks for not using this dice rolling simulator ")

	

else:

	print("Please type a valid input!")

	

	

	
