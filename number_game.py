# to import the random library
import random

x = 1
y = 10
	
def play_game():

	print("Guess the number between {} and {}. You have 3 chances".format(x, y))
	number = random.randint(x,y)
	countdown = 3

	while countdown:
		try:
			guess = int(input())
		except ValueError:
			print("That's not a number. Please try again.")
		else:
			if guess < number:
				print("Not the correct number. The number is higher.")
			elif guess > number:
				print("Not the correct number. The number is lower.")
			else:
				break
			countdown -= 1

	if number == guess:
		print("Congratulations! You guessed the number!")
	else:
		print("Your chances are over : (")

	print("The number is {}.".format(number))

	play_again = input("Would you like to play again? Y / N").lower()
	if play_again != 'n':
		play_game()
	else:
		print("Come back later!")

play_game()