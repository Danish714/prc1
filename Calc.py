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
print("asfjdhasjkdf ")
# Predefined values
num1 = input("fesfsdj jlhl")
num2 = 7

# Perform operations
result_multiply = multiply(num1, num2)
result_subtract = subtract(num1, num2)
result_add = add(num1, num2)
result_divide = divide(num1, num2)

# Display results
print(f"Multiplication: {num1} * {num2} = {result_multiply}")
print(f"Subtraction: {num1} - {num2} = {result_subtract}")
print(f"Addition: {num1} + {num2} = {result_add}")
print(f"Division: {num1} / {num2} = {result_divide}")
