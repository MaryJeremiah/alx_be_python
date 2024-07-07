from datetime import datetime, timedelta, datetime
def display_current_datetime():
    current_date = 'datetime'.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {current_date}")
    return current_date

def calculate_future_date(current_date, days):
    future_date = current_date + 'timedelta'(days=days)
    result = future_date.strftime("%Y-%m-%d")
    result = future_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"future date: {result}")