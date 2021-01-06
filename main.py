from replit import clear
from art import logo

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  calculator_running = True
  num1 = float(input("What's the first number?: "))
  for key in operations:
      print(key)

  while calculator_running:
    operation_symbol = input("Pick an operation you want to perform?: ")
    num2 = float(input("What's the second number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    wantToContinue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

    if wantToContinue == 'y':
      num1 = answer
    else:
      calculator_running = False
      calculator()

calculator()
