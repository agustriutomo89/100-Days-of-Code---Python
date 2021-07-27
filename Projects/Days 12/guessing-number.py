#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

WELCOME_MESSAGE="Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
DIFFICULTY_MESSAGE="Choose a difficulty. Type 'easy' or 'hard':"
GUESS_MESSAGE="Make a guess:"
AGAIN_MESSAGE="Guess Again"
TOO_HIGH_MESSAGE="Too High!"
TOO_LOW_MESSAGE="Too Low!"
EASY_DIFFICULTY="easy"

print(logo)
print(WELCOME_MESSAGE)
difficulty=input(DIFFICULTY_MESSAGE).lower()

max_attempts=5

if difficulty == EASY_DIFFICULTY:
  max_attempts=10

correct_answer = random.randint(1,100)

while max_attempts > 0:
  print(f"You have {max_attempts} remaining to guess the number.")
  guess=int(input(GUESS_MESSAGE))

  if guess == correct_answer:
    print(f"You got it! The answer was {guess}")
    break
  elif guess > correct_answer:
    print(TOO_HIGH_MESSAGE)
    print(AGAIN_MESSAGE)
  else:
    print(TOO_LOW_MESSAGE)
    print(AGAIN_MESSAGE)

  max_attempts -= 1

if max_attempts == 0:
  print(f"You Lose! The correct number is {correct_answer}")