

#Add operation
def add(n1,n2):
  return n1+n2

#Substract operation
def substract(n1,n2):
  return n1-n2

#Multiply operation
def multiply(n1,n2):
  return n1*n2

#Divide operation
def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-":substract,
  "*":multiply,
  "/":divide
}

def calculator():
  num1 = int(input("What's the first number?: "))
  for key in operations:
    print(key)
  operation_symbol= input("Pick an operation from the line above: ")

  num2 = int(input("What's the second number?: "))

  function = operations[operation_symbol]

  answer=function(num1,num2)
  previousAnswer = answer 
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  isNotDone = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:")

  while isNotDone == "y":
    operation_symbol= input("Pick an operation:")
    nextNumber=int(input("What's the next number? :"))

    function = operations[operation_symbol]
    answer=function(previousAnswer,nextNumber)
    print(f"{previousAnswer} {operation_symbol} {nextNumber} = {answer}")
    previousAnswer = answer 

    isNotDone = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:")
    if isNotDone == "n":
      calculator()

calculator()