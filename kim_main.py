import sys
import time
from pynput import keyboard
from kim import Kim


kim = Kim()
clock = time.asctime() #Gives actuall time back

def on_press(key):
    try:
        char = None
        if hasattr(key, 'char'):
            char = key.char
        else:
            char = key.name
        
        if char == 's':
            kim.start()
            print("\n",clock.center(50))
            print("\n[KIM] Is running {°o°}")
        
        elif char == 'p':
            kim.pause()
            print("\n[KIM] Is resting {≠,≠}")
        
        elif char == 'r':
            kim.resume()
            print("\n[KIM] Is running agian {°o°}")
        
        elif key == keyboard.Key.esc:
            print("\n[KIM] Says Goodbye see ya {^_^}")
            kim.clean_exit()
            sys.exit()
            
    except AttributeError:
        print('[KIM] Is confused @,@...')
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print("Thread Status:", kim.is_alive())
