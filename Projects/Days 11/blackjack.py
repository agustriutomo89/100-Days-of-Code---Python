from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computerLimit = 17 
maxScore = 21
stillPlaying = True
playerListCard = []
dealerListCard = []

#pre init

def preInitListCard():
  playerListCard.append(random.choice(cards))
  playerListCard.append(random.choice(cards))
  dealerListCard.append(random.choice(cards))
  dealerListCard.append(random.choice(cards))

preInitListCard()
print(logo)

### 1 --> player wins
### 2 --> player 2 wins 
### 3 --> draw 
def checkWhoWins(list1,list2):
  totalList1 = sum(list1)
  totalList2 = sum(list2)

  if totalList1 == totalList2:
    return 3
  elif totalList1 == 21:
    return 1
  elif totalList2 == 21:
    return 2
  elif totalList1 > 21 and totalList2 < 21:
    return 2
  elif totalList2 > 21 and totalList1 < 21:
    return 1
  elif 21-totalList1 > 21-totalList2:
    return 2
  else:
    return 1

def printWinner(statusWinner):
  if(whoWins == 1):
    print("You Win")
  elif(whoWins == 2):
    print("You Lose")
  else:
    print("draw")

tempInput=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if(tempInput == "y"):
  stillPlaying= True
else:
  stillPlaying= False

while stillPlaying:
  print("Your cards", playerListCard, " current score:", sum(playerListCard))
  print("Computer first card:", dealerListCard[0])

  if sum(playerListCard) < maxScore or sum(dealerListCard) < maxScore:
    stillDrawCard=input("Type 'y' to get another card, type 'n' to pass:")
    whoWins=-1
    while stillDrawCard == "y":
      playerListCard.append(random.choice(cards))

      #get card for dealer
      if(sum(dealerListCard) < computerLimit):
        dealerListCard.append(random.choice(cards))

      if sum(playerListCard) > maxScore or sum(dealerListCard) > maxScore:
        print("Your final hands", playerListCard, " final score:", sum(playerListCard))
        print("Computer final hand:", dealerListCard, " final score:", sum(dealerListCard))
        whoWins=checkWhoWins(playerListCard,dealerListCard)
        printWinner(whoWins)
        stillDrawCard="n"
      else:
          print("Your cards", playerListCard, " current score:", sum(playerListCard))
          print("Computer first card:", dealerListCard[0])
          stillDrawCard=input("Type 'y' to get another card, type 'n' to pass:")
      
    if(whoWins == -1 ):
      while sum(dealerListCard) < computerLimit:
        dealerListCard.append(random.choice(cards))

      print("Your final hands", playerListCard, " final score:", sum(playerListCard))
      print("Computer final hand:", dealerListCard, " final score:", sum(dealerListCard))
    
      whoWins=checkWhoWins(playerListCard,dealerListCard)
      printWinner(whoWins)

    tempInput=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if(tempInput == "y"):
      stillPlaying= True
      playerListCard = []
      dealerListCard = []
      preInitListCard()
    else:
      stillPlaying= False


  

 
  







############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
