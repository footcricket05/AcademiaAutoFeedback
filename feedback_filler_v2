from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def press_key(key, times=1, delay=0.1):
    for _ in range(times):
        keyboard.press(key)
        time.sleep(delay)
        keyboard.release(key)

def fill_feedback():
    press_key(Key.down, times=10)
    press_key(Key.tab)

print("Get ready, and point your cursor at the first index position...")
time.sleep(3)

while True:
    fill_feedback()  # Fill feedback for the first index position
