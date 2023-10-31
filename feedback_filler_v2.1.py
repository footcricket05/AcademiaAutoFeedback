from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def press_keys(keys, delay=0.1):
    for key in keys:
        keyboard.press(key)
        time.sleep(delay)
        keyboard.release(key)

def fill_feedback():
    keys_to_press = [Key.down] * 10 + [Key.tab]
    press_keys(keys_to_press)

print("Get ready, and point your cursor at the first index position...")
time.sleep(3)

while True:
    fill_feedback()  # Fill feedback for the first index position
