try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: please enter valid numbers.")


# Ask user to choose an operation
print("\nAvailable operations:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

operation = input("\nChoose an operation (add/subtract/multiply/divide): ").lower()

# Perform the selected operation
if operation == "add":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "subtract":
    result = num1 -num2 
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "divide":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
else:
    print("Error: Invalid operation. Please choose add, subtract, multiply, or divide.")

if __name__ == "__main__":
    print("Simple Calculator")



