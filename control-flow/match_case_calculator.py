num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

chosen_operation = input("Choose the operation (+, -, *, /):")

match chosen_operation:
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
        result = num1 / num2
        if num2 >0:
            print(f"The result is {result}")
        else:
            print(f"Cannot divide by zero")
    case _:
        print("Invalid operation chosen")
    