#Conversion factor for Fahrenheit to Celsius
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

#Conversion factor for Celsius to Fahrenheit
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):

    # Converts temperature from Fahrenheit to Celsius
    celsius_converion = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius_converion

def convert_to_fahrenheit(celsius):

    # Converts temperature from Celsius to Fahrenheit
    fahrenheit_conversion = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit_conversion

def main():

    while True:
        user_option = input("Select 'q' to quit program or 'c' to continue: ").strip().lower()
        if user_option == "q":
            break

        elif user_option == "c":

            temperature = float(input("Enter the temperature to convert: "))
            unit_to_convert = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

            if unit_to_convert == "F":
                converted_temperature = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temperature}°C")

            elif unit_to_convert == "C":
                converted_temperature = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temperature}°F")

            else: 
                print("Error: Select the correct option from the menu")


if __name__ == "__main__":
    main()