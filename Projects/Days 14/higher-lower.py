from art import logo
from art import vs
from game_data import data 
import random

QUESTION="Who has more followers? Type 'A' or 'B':"
INDEX_NAME="name"
INDEX_DESCRIPTION="description"
INDEX_COUNTRY="country"
INDEX_FOLLOWERCOUNT="follower_count"

def printCurrentStatus(status,score):
  if status == True:
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")

def printData(side,index):
  name=data[index][INDEX_NAME]
  description=data[index][INDEX_DESCRIPTION]
  country=data[index][INDEX_COUNTRY]
  print(f"Compare {side}: {name}, a {description}, from {country}.")

def compareTotalFollower(followerA,followerB):
  if followerA > followerB:
    return "A"
  return "B"

def getTotalFollower(index):
  return data[index][INDEX_FOLLOWERCOUNT]

currentScore=0
currentIndexDataWinner=random.randint(0,len(data)-1)
currentIndexOpponent=0
isStillWin = True


while isStillWin:
  print(logo)
  currentIndexOpponent=random.randint(0,len(data)-1)

  if currentScore > 0:
    printCurrentStatus(True,currentScore)

  printData("A",currentIndexDataWinner)
  print(vs)
  printData("B",currentIndexOpponent)
  chosen=input(QUESTION)

  totalFollowerA=getTotalFollower(currentIndexDataWinner)
  totalFollowerB=getTotalFollower(currentIndexOpponent)
  winner=compareTotalFollower(totalFollowerA,totalFollowerB)

  if chosen == winner:
    currentScore+=1
    
    if winner == "A":
      currentIndexDataWinner=currentIndexDataWinner
    else:
      currentIndexDataWinner=currentIndexOpponent
  else:
    printCurrentStatus(False,currentScore)
    break


