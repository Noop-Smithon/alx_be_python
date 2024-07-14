def safe_divide(numerator, denominator):
    try:
        dividend = float(numerator)
        divisor = float(denominator)
        if divisor == 0:
            return "Error: Cannot divide by zero."
        result = dividend / divisor
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."