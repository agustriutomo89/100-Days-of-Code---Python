# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

totalLengthNames = len(names)
randomNumber = random.randint(0,totalLengthNames-1)
chosenName = names[randomNumber]

print(f"{chosenName} is going to buy the meal today!")




