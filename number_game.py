# to import the random library
import random

x = 1
y = 10
	
print("Guess the number between {} and {}.".format(x, y))

number = random.randint(x,y)

guess = None

while guess != number:

	guess = int(input())

	if guess < number:
		print("Not the correct number. Guess higher.")
	elif guess > number:
		print("Not the correct number. Guess lower.")
	else:
		print("Congratulations! You guessed the number!")