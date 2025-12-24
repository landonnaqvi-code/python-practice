import random

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  secret_number = random.randint(1, 100)
  attempts = 0

  while True:
    user_guess = input("Enter your guess(or type quit to exit)")
    if user_guess.lower() == "quit":
      break
    elif not (user_guess % 1 == 0):
      print("Please enter a valid integer number")
      break

game()
