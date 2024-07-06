def perform_operation(num1, num2, operation):

    """_This function will be used to perform basic arithmetic operations (addition, subtraction, multiplication and division) based off the user's input following a prompt._

    Args:
        num1 (float): _description_
        num2 (float): _description_
        operation (string): _description_
    """

    # Execute operation based on user input
    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        # handle division_by_zero error
        if num2 == 0:
            print("Error: Division by zero not possible")
        else:
            return num1 / num2

    else:
        return "Error: Invalid Operation Selected"


def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()