import re
from datetime import datetime
import pytz

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email)

email = input("Enter your email address: ")

if is_valid_email(email):
    print("Email is valid.")
else:
    print("Invalid email format.")

timezone = ['UTC', 'US/Eastern', 'Europe/London', 'Asia/Riyadh', 'Asia/Kolkata', 'Australia/Sydney']

print("\n🕒 Current Time in Different Timezones:")
for zone in timezone:
    timezone = pytz.timezone(zone)
    time_in_zone = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    print(f"{zone}: {time_in_zone}")