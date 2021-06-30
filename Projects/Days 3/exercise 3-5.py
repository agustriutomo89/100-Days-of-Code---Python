# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#count TRUE 
name1Lowered = name1.lower() 
name2Lowered = name2.lower() 

firstDigitTotal = 0
firstDigitTotal += name1Lowered.count("t")
firstDigitTotal += name1Lowered.count("r")
firstDigitTotal += name1Lowered.count("u")
firstDigitTotal += name1Lowered.count("e")

firstDigitTotal += name2Lowered.count("t")
firstDigitTotal += name2Lowered.count("r")
firstDigitTotal += name2Lowered.count("u")
firstDigitTotal += name2Lowered.count("e")

#count LOVE

secondDigitTotal = 0
secondDigitTotal += name1Lowered.count("l")
secondDigitTotal += name1Lowered.count("o")
secondDigitTotal += name1Lowered.count("v")
secondDigitTotal += name1Lowered.count("e")

secondDigitTotal += name2Lowered.count("l")
secondDigitTotal += name2Lowered.count("o")
secondDigitTotal += name2Lowered.count("v")
secondDigitTotal += name2Lowered.count("e")

totalScoreString = str(firstDigitTotal) + str(secondDigitTotal)
totalScoreInt = int(totalScoreString)

if totalScoreInt < 10 or totalScoreInt > 90:
  print(f"Your score is {totalScoreInt}, you go together like coke and mentos.")
elif totalScoreInt >= 40 and totalScoreInt <= 50:
  print(f"Your score is {totalScoreInt}, you are alright together.")
else:
  print(f"Your score is {totalScoreInt}.")