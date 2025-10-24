#import datetime module to display date and time
from datetime import datetime, timedelta

#define function to display current date and time
def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

#funtion to add days to current date
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Date after {number_of_days} days will be:", future_date.strftime("%Y-%m-%d"))

display_current_datetime()
calculate_future_date()