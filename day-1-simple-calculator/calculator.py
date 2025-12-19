# Get input Values - Variables. 

# Get user intent
print("""
1. Addition \n
2. Subtraction \n
3. Multiplication \n
4. Division \n
5. Press 5 to exit.
""")

calculator_condition = True

while calculator_condition:
	print("\n")
	print("Welcome to calculator !")

	user_operation = int(input("Enter your option: "))

	if user_operation == 1:
		# Addition Logic
		print("Addition")
		number_1 = int(input(" Enter number 1 "))
		number_2 = int(input(" Enter number 2 "))
		result = number_1 + number_2
		print("The result is", result)
		
	elif user_operation == 2:
		# Sub Logic
		print("Subtract")
		number_1 = int(input(" Enter number 1 "))
		number_2 = int(input(" Enter number 2 "))
		result = number_1 - number_2
		print("The result is", result)
		
	elif user_operation == 3:
		# Multiplication
		print("Multiplication")
		number_1 = int(input(" Enter number 1 "))
		number_2 = int(input(" Enter number 2 "))
		result = number_1 * number_2
		print("The result is", result)
		
	elif user_operation == 4:
		# Division
		print("Division")
		number_1 = int(input(" Enter number 1 "))
		number_2 = int(input(" Enter number 2 "))
		result = number_1 / number_2
		print("The result is", result)
	
	elif user_operation == 5:
		print("Thanks for using calculator ! See you again.")
		calculator_condition = False
