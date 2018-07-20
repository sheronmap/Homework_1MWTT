# favourite number

favourite_number = input("What is your favourite number? ")

try:
	if type(eval(favourite_number)) ==int:
		new_favourite_number = int(favourite_number) + 1
		print("Your favourite number sucks! Try "+str(new_favourite_number)+" , it's a bigger and better number!")
	elif type(eval(favourite_number)) ==float:
		new_favourite_number = float(favourite_number) + 1
		print("Your favourite number sucks! Try "+str(new_favourite_number)+" , it's a bigger and better number!")
	else:
		print("You have not entered a number, please enter a number. ")
except: print("You have not entered a number, please enter a number. ")		

		
