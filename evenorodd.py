def check_even_odd():
    # Get user input
    num = int(input("Enter a number: "))

    # Check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Run the function
check_even_odd()