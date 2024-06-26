import threading
import time
import pyautogui
import sys
import random

class Kim(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.paused = False
        self.running = True
        self.pause_condition = threading.Condition(threading.Lock())
        self.mlists = self.create_mlists()
        
        
        
    def create_mlists(self):
        mlist_1 = [{"x": 0, "y": -50}, {"x": 50, "y": 0}, {"x": -50, "y": 0}, {"x": 0, "y": 50}]
        mlist_2 = [{"x": 0, "y": 50}, {"x": -50, "y": 0}, {"x": 50, "y": 0}, {"x": 0, "y": -50}]
        #mlist_X = [{"x: 0, "y": 0}, {"x: 0, "y": 0}]

        return [mlist_1, mlist_2]

    def run(self):
        while self.running:
            with self.pause_condition:
                while self.paused:
                    self.pause_condition.wait()

                selected_movement = random.choice(self.mlists)
                
                for koord in selected_movement:
                    self.move_mouse(koord["x"], koord["y"])
                #smooth mice flow.
                time.sleep(1)

                self.mlists = self.create_mlists()

            time.sleep(5) #in sec| Default for purpose '90'

    def pause(self):
        with self.pause_condition:
            self.paused = True

    def resume(self):
        with self.pause_condition:
            self.paused = False
            self.pause_condition.notify()

    def move_mouse(self, x, y):
        current_x, current_y = pyautogui.position()
        new_x, new_y = current_x + x, current_y + y
        pyautogui.moveTo(new_x, new_y)

    def clean_exit(self):
        self.running = False
        with self.pause_condition:
            self.pause_condition.notify() # Ensure thread can exit if paused

    
    def is_running(self):
        return not self.paused and self.running

    def stop(self):
        self.clean_exit()
        print("\n[KIM] Stops {x_x}")



# Bewege den Cursor nach oben
# Bewege den Cursor nach rechts
# Bewege den Cursor nach links
# Bewege den Cursor nach unten