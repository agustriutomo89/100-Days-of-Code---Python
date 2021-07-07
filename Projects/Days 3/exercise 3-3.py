# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leapYear = "Leap year."
notLeapYear = "Not leap year."

if year % 4 == 0:
  if year % 100 != 0:
    print(leapYear)
  else:
    if year % 400 == 0:
      print(leapYear)
    else:
      print(notLeapYear)
else:
  print(notLeapYear)


