import sys
import time
from pynput import keyboard
from kim import Kim
from datetime_utils import clock, calender, iso_8601_t, iso_8601_c

              #USE#
#-------------------------------#

#--calls functions from kim-----#    
kim = Kim()

#--calls actual date and time---#
#--calls format for date and time--#
hour_now = clock.hour()
minute_now = clock.minute()
second_now = clock.second()

day_today = calender.day()
month_today = calender.month()
year_today = calender.year()

iso_hour, iso_minute = iso_8601_t(hour_now, minute_now)
iso_date = iso_8601_c(day_today, month_today, year_today)
#-------------------------------#


def on_press(key):
    try:
        char = None
        if hasattr(key, 'char'):
            char = key.char
        else:
            char = key.name
        
        if char == 's':
            kim.start()
            print(f"\nIt´s {iso_hour}:{iso_minute} o´clock.".center(50))
            print("\n[KIM] Is running {°o°}")
        
        elif char == 'p':
            kim.pause()
            print("\n[KIM] Is resting {≠,≠}")
        
        elif char == 'r':
            kim.resume()
            print("\n[KIM] Is running agian {°o°}")
        
        elif key == keyboard.Key.esc:
            print("\n[KIM] Says Goodbye see ya {^_^}")
            print(f"\nIt´s {iso_hour}:{iso_minute} o´clock.".center(50))
            kim.clean_exit()
            sys.exit()
            
    except AttributeError:
        print('[KIM] Is confused @,@...')
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print("Thread Status:", kim.is_alive())
