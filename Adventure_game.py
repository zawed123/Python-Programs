#https://www.facebook.com/100051921408118/posts/190716086002437/?app=fbl
#Subscribed by CodeHouse
print("--------Welcome to this adventure game-------")

name = input("What is your name? ")

age = int(input("What is your age? \n"))

if age>=18:

	print("You are old enough to play this game :)\n\n")

	

	choice1=input("You found yourself in a dark forest.\nYou see there is a campfire in your left and an abandoned barn  in your right.\nWill you go left or right?(left/right) ")

	if choice1=="left":

		print("You survived and no wild animal came near you\n\n")

		

		print("Now its morning and you have to cross the whole forest.")

		print("You started to move ahead.") 			

		choice2 = input("But there's a mountain in your left and river in your right.\nSo where will you go? ")

		

		if choice2=="right":

			print("You survived again and crossed the river because river was not too deep.\n\n")

			

			choice3=input("Now you are almost ouside of the forest.\nAnd you saw a road in your left and shortcut to get outside of the forest in your right.\nSo where will you go?(left/right) ")

			if choice3=="right":

				print("You finally made it out of the forest.\n\n")

				

			elif choice3=="left":

				print("Oh you just hit by a truck running at very high speed")

			

		elif choice2=="left":

			print("You died by felling because the mountain was too steep")

		

		

	elif choice1=="right":

		print("You died because there were hungry wolves in the barn")

		

else:

	print("Your are not old enough to play this game :(")

	
