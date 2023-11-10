import random
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 to 100")


def guess_number():
  guessed_number = random.randint(1,100)
  return guessed_number

random_num = guess_number()
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if(difficulty == 'easy'):
  num_of_guesses = 10
elif(difficulty == 'hard'):
  num_of_guesses = 5

continue_guessing = True

while continue_guessing:
  user_num = int(input(f"Enter your guess. You have {num_of_guesses} attempts remaining. :P"))

  if user_num > random_num:
    print("Too high\nGuess again.")
  elif user_num < random_num:
    print("Too low\nGuess again.")
  else:
    print(f"You guessed right! the number was {random_num} :)")
    continue_guessing = False
  

  if num_of_guesses == 1:
    continue_guessing = False
    print(f"You ran out of guesses :( the number was {random_num}")

  num_of_guesses -= 1

