num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        while num2 == 0:
            print(f"Cannot divide by zero")
            num1 = int(input("Enter the first number:"))
            num2 = int(input("Enter the second number:"))
            chosen_operation = input("Choose the operation (+, -, *, /):")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation chosen")
    