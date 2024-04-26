""""
#Timer function to definve aktuall time.
from datetime import datetime, date, timezone
import time


d_now = datetime.now()

print("Wir haben:",d_now.hour,":",d_now.minute, '\n' "Und den:", d_now.day, d_now.month, d_now.year)
"""
from datetime import datetime

quant = datetime.now()

class Clock():
    def hour(self):
        return quant.hour
    
    def minute(self):
       return quant.minute
    
    def second(self):
        return quant.second

class Calender():
    def day(self):
        return quant.day
    
    def month(self):
        return quant.month

    def year(self):
        return quant.year

clock = Clock()
calender = Calender()

"""
hour_now = clock.hour()
minute_now = clock.minute()
second_now = clock.second()

day_today = calnder.day()
month_today = calnder.month()
year_today = calnder.year()
"""

def iso_8601_t(hour, minute): #function for formated time for 00-09
    iso_hr = f"{hour:02d}" #hour with zero infront
    iso_min = f"{minute:02d}" #minute with zero infront
    return iso_hr, iso_min

def iso_8601_c(day, month, year): #function for formated dates
    return f"{day:02d}.{month:02d}.{year}"
"""
iso_hour, iso_minute = iso_8601_t(hour_now, minute_now)
iso_date = iso_8601_c(day_today, month_today, year_today)
"""