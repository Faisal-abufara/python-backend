from datetime import datetime
import pytz

date_str = input("Enter date/time (YYYY-MM-DD HH:MM): ")
from_tz = input("From timezone (e.g. Asia/Riyadh): ")
to_tz = input("To timezone (e.g. UTC): ")

from_zone = pytz.timezone(from_tz)
to_zone = pytz.timezone(to_tz)


dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
dt = from_zone.localize(dt)

converted = dt.astimezone(to_zone)
print(f"\n⏱ Converted time in {to_tz}: {converted.strftime('%Y-%m-%d %H:%M:%S')}")