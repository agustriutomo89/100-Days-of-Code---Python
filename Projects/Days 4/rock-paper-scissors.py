import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice= input("What do you choose? 0 for Rock, 1 for Paper, and 2 for Scissors? ")
user_choice_int = int(user_choice)

listChoice = ["Rock", "Paper", "Scissors"]
listChoiceASCI = [rock,paper,scissors]

print("You choose ", listChoice[user_choice_int])
print(listChoiceASCI[user_choice_int])

computerChoice = random.randint(0,2)

# 0 --> Lose, 1 --> Win, 2 --> Draw
gameState = 0

if user_choice_int == 2:
  if(computerChoice == 0):
    gameState = 0
  elif(computerChoice == 1):
    gameState = 1
  else:
    gameState = 2
elif user_choice_int == computerChoice:
  gameState = 2
elif user_choice_int + 1 == computerChoice:
  gameState = 0
elif user_choice_int + 2 >= computerChoice:
  gameState = 1
else:
  gameState = 0

print("Computer choose ", listChoice[computerChoice])
print(listChoiceASCI[computerChoice])

if gameState == 0:
  print("You lose! Computer Win")
elif gameState == 1:
  print("You Win! Computer lose")
else:
  print("Draw!")