#Write your code below this line 👇

def prime_checker(number):
  isPrimeNumber = False

  if number <= 1 or number == 2:
    isPrimeNumber=False
  elif number % 2 == 0:
    isPrimeNumber=True
  else:
    i = 3
    while i < number:
      #print(i)
      if number % i == 0:
        isPrimeNumber = False
        break
      i=i+1
  
  if isPrimeNumber:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



