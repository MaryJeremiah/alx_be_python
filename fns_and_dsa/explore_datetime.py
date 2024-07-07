from datetime import datetime, timedelta, datetime
def display_current_datetime():
    date = datetime.now()
    current_date = date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    return current_date

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    delta = timedelta(days=number_of_days)
    day = datetime.now() + delta
    future_date = day + delta
    result = future_date.strftime("%Y-%m-%d")


    print(f"future date: {result}")