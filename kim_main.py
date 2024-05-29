import sys
from datetime import datetime
from pynput import keyboard
from kim import Kim


              #USE#
#-------------------------------#

#--calls functions from kim-----#    
kim = Kim()


#-------------------------------#
def get_formatted_time(): #function for dynamic time registration
    now = datetime.now()
    return now.strftime("%H:%M")
#-------------------------------#

def on_press(key):
    global listener
    try:
        char = None
        if hasattr(key, 'char'):
            char = key.char
        else:
            char = key.name
        
        if char == 's':
            kim.start()
            start_time = get_formatted_time()
            print("\n[KIM] Is running {°o°}" f" at : {start_time}")
        
        elif char == 'p':
            kim.pause()
            resting_time = get_formatted_time()
            print("\n[KIM] Is resting {≠,≠}" f": {resting_time}")
        
        elif char == 'r':
            kim.resume()
            rerunn_time = get_formatted_time()
            print("\n[KIM] Is running agian {°o°}" f": {rerunn_time}")
        
        elif key == keyboard.Key.esc:
            end_time = get_formatted_time()
            print("\n[KIM] Says Goodbye see ya {^_^}" f" at: {end_time}")
            
            kim.clean_exit()
            listener.stop() #stops the keayboard-listener
            sys.exit()
            
    except AttributeError:
        print('[KIM] Is confused @,@...')
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


#--Status Tracker--#
#print("Thread Status:", listener.is_alive()) #checks keyboard-listener / Ture = processin | False = no processing
#------------------#