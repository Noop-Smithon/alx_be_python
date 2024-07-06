from datetime import datetime, timedelta

current_date = datetime.now()

def display_current_datetime():

    # Retrieve and print current date and time in readable format.
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):

    #Calculate future date based on number of days (greater than zero) provided by user
    future_date = current_date + timedelta(days=days)
    return future_date


def main():

    #Carries out the program execution by calling functions where needed
    display_current_datetime()

    while True:
        option = input("Select 'q' to quit program or 'c' to continue: ").strip().lower()
        if option == "q":
            break
        elif option == "c":
            days = int(input("Enter the number of days to add to the current date: "))
            if days <= 0:
                print("please select a number greater than zero to view future date")
            else:
                future_date = calculate_future_date(days)
                formatted_future_date = future_date.strftime("%Y-%m-%d")
                print(f"future date: {formatted_future_date}")
        else:
            print("Invalid input selected; Please select the correct input from the menu")

if __name__ == "__main__":
    main()