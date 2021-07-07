from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
bidders={}

isContinue=True

while isContinue:
  name=input("What is your name?")
  bid=int(input("What's your bid? $"))

  bidders[name]=bid

  bidAgain=input("Are there any other bidders? Type 'yes' or 'no'.")
  if bidAgain == "no":
    isContinue= False

winner=""
bid=0
for key in bidders:
  if bidders[key] > bid:
    bid=bidders[key]
    winner=key

print(f"The winner is {winner} with a bid of ${bid}")