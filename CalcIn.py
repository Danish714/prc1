def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def add(a, b):
    return a + b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."


num1 = int(input("entr first nbr   "))
num2 = int(input("enter second nbr  "))
operand=input("enter operand  ")


# Perform operationsgit
if operand=="+":
    result = multiply(num1, num2)
if operand=="-":
    result = subtract(num1, num2)
if operand=="*":
    result = add(num1, num2)
if operand=="/":
    result = divide(num1, num2)

# Display results
print(f"{num1} {operand} {num2} = {result}")
 