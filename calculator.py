num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero")
        exit()
    result = num1 / num2
else:
    print(f"Error: Unknown operator '{operator}'")
    exit()

print(f"{num1} {operator} {num2} = {result}")
