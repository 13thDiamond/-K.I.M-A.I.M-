import sys
from datetime import datetime
from pynput import keyboard
from kim import Kim
import threading



#-------------------------------#
def get_formatted_time(): #function for dynamic time registration
    now = datetime.now()
    return now.strftime("%H:%M")


#-------------------------------#
def run_kim_program(stop_event):
    kim = Kim()

    def on_press(key):
        try:
            char = None
            if hasattr(key, 'char'):
                char = key.char
            else:
                char = key.name
            
            if char == 's':
                if not kim.is_alive():
                    kim.start()
                    start_time = get_formatted_time()
                    print("\n[KIM] Is running {°o°}" f" at : {start_time}")
            
            elif char == 'p':
                if kim.is_alive() and kim.is_running():
                    kim.pause()
                    resting_time = get_formatted_time()
                    print("\n[KIM] Is resting {≠,≠}" f": {resting_time}")
            
            elif char == 'r':
                if kim.is_alive() and not kim.is_running():
                    kim.resume()
                    rerun_time = get_formatted_time()
                    print("\n[KIM] Is running agian {°o°}" f": {rerun_time}")
            
            elif key == keyboard.Key.esc:
                if kim.is_alive():
                    end_time = get_formatted_time()
                    print("\n[KIM] Says Goodbye see ya {^_^}" f" at: {end_time}")
                    kim.clean_exit()
                    stop_event.set() #stops the keayboard-listener
                    return
                    
        except AttributeError:
            print('[KIM] Is confused @,@...')
            pass

    #with keyboard.Listener(on_press=on_press) as listener:
        #listener.join()
    listener = keyboard.Listener(on_press = on_press)
    listener.start()

    stop_event.wait()
    if listener.is_alive():
        listener.stop()

def main():
    while True:
        stop_event = threading.Event()
        run_kim_program(stop_event)
        user_input = input("\nTo quit K.I.M write 'yes' and confirm with enter\n"
              "To restart K.I.M write 'restart' and confirm with enter.\n").strip().lower()
        

        if user_input == 'yes':
            end_time = get_formatted_time()
            print("\n KIM shuts down!" f"{end_time}")
            break
        elif user_input == 'restart':
            print("\n KIM is restarting!")
        else:
            end_time = get_formatted_time()
            print("\n Undifined input. Application shut down!" f"at {end_time}")
            break

if __name__ == "__main__":
    main()


#--Status Tracker--#
#print("Thread Status:", listener.is_alive()) #checks keyboard-listener / Ture = processin | False = no processing
#------------------#