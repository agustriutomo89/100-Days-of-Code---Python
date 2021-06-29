#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10,12, or 15? ")
total_person = input("How many to split the bill? ")

percentage_tip_int = float(total_bill) * 12 / 100
total_bill_with_tip = float(total_bill) + percentage_tip_int
total_pay_per_person = round(total_bill_with_tip/int(total_person),2)

print(f"Each person should pay: ${total_pay_per_person}")

