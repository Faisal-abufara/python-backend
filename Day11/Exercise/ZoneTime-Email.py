from datetime import datetime
import pytz

utc_time = datetime.now(pytz.utc)
ksa_time = utc_time.astimezone(pytz.timezone('Asia/Riyadh'))
jordan_time = utc_time.astimezone(pytz.timezone('Asia/Amman'))

print("Utc tiem: " , utc_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Utc tiem: " , ksa_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Utc tiem: " , jordan_time.strftime("%Y-%m-%d %H:%M:%S"))