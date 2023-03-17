
from art import logo
def add(n1,n2):
   return n1+n2
   
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
math_sign={ "+": add,  "-" : subtract,  "*" : multiply,  "/": divide}


def calc():
  
  print(logo)
  num1= float(input("What is the first number:"))

  for sign in math_sign:
    print(sign)
  
  should_continue=True

  while should_continue:

    operational_sign=input("Pick an operation from the line above:")

    num2= float(input("What is the second number:"))

    calculation_function= math_sign[operational_sign]
    answer= calculation_function(num1,num2)

    print(f"{num1} {operational_sign} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation:") =="y":
       num1=answer
    else:
      should_continue=False
      calc()

calc()