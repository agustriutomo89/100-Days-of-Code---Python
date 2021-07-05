#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO 1
total_length_word_list = len(word_list)
chosen_word_index = random.randint(0,total_length_word_list-1)
chosen_word = word_list[chosen_word_index]

#TODO 2
guess=str.lower(input("Guess a letter? "))

#TODO 3
for i in range(0,len(chosen_word)):
  if guess == chosen_word[i]:
    print("RIGHT")
  else:
    print("WRONG")