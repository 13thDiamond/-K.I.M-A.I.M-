import threading
import time
import pyautogui
import sys

class Kim(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.paused = False
        self.pause_condition = threading.Condition(threading.Lock())
        self.movements = [
            [{"x": 0, "y": -50}, {"x": 50, "y": 0}, {"x": -50, "y": 0}, {"x": 0, "y": 50}], #List 1
            [{"x": 0, "y": 50}, {"x": -50, "y": 0}, {"x": 50, "y": 0}, {"x": 0, "y": -50}], #List 2
            #[{"x: 0, "y": 0}, {"x: 0, "y": 0}],....Enter another movmentlist....
        ]

    def run(self):
        while True:
            with self.pause_condition:
                while self.paused:
                    self.pause_condition.wait()

                for movement in self.movements:
                    for koord in movement:
                        self.move_mouse(koord["x"], koord["y"])

            time.sleep(5) #in sec| Default for purpose '90'

    def pause(self):
        self.paused = True
        self.pause_condition.acquire()

    def resume(self):
        self.paused = False
        self.pause_condition.notify()
        self.pause_condition.release()

    def move_mouse(self, x, y):
        current_x, current_y = pyautogui.position()
        new_x, new_y = current_x + x, current_y + y
        pyautogui.moveTo(new_x, new_y)

    def clean_exit(self):
        sys.exit()

    def stop(self):
        print("\n[KIM] Stops {x_x}")

# Bewege den Cursor nach oben
# Bewege den Cursor nach rechts
# Bewege den Cursor nach links
# Bewege den Cursor nach unten