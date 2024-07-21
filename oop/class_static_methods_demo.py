class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Returns the sum of two numbers.
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Returns the product of two numbers and prints tge class attribute "calculation_type."
        print(f"Calculation type: {cls.calculation_type}")
        return a * b