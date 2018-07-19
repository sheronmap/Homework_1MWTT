# favourite number

favourite_number = input("What is your favourite number?")

#if favourite_number.isdigit():
if type(eval(favourite_number)) == int:
	new_favourite_number = int(favourite_number) + 1
	print("Your favourite number sucks! Try "+str(new_favourite_number)+" for a favourite!")
else:
	print("You have not entered a number, please enter a number. ")
