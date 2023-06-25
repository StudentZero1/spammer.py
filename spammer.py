import pyautogui
import datetime
import time

message = "Hello World"
num_iterations = 10 #Replace with how many messages you would like to send

# Set the desired start time
start_hour = 00  # Replace with your desired start hour (in 24-hour format)
start_minute = 00  # Replace with your desired start minute
start_second = 00 # Replace with your desired start second

# Get the current time
current_time = datetime.datetime.now()

# Set the start time for today
start_time = current_time.replace(hour=start_hour, minute=start_minute, second=start_second)

# Check if the start time has already passed for today
if current_time > start_time:
    # Increment the start time by one day if it has already passed
    start_time += datetime.timedelta(days=1)

# Calculate the time difference between the current time and the start time
time_difference = start_time - current_time

# Delay before starting
time.sleep(time_difference.total_seconds())

try:
    for i in range(num_iterations):
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        time.sleep(0.1)  # Delay between each iteration (adjust as needed)
        if i + 1 == num_iterations:
            break

    print("No errors found")
except Exception as e:
    print(f"An error occurred: {str(e)}")
# I take no responsability for your actions 
