#!/usr/bin/env python3
import os
import pyautogui
from Xlib import display as Xlib_display
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests

import subprocess
pyautogui._pyautogui_x11._display = Xlib_display.Display(os.environ['DISPLAY'])
def execute_xdotool_command(command):
    subprocess.run(["xdotool"] + command.split())


from time import sleep
if __name__ == "__main__":
    sleep(10)
    # Perform automation tasks
    pyautogui.hotkey("ctrl", "l")  # Press Ctrl+L
    pyautogui.typewrite("https://www.example.com")  # Type the web address
    pyautogui.press("enter")  # Press Enter

    if os.getenv("NO_SLEEP") == "1":
        if "APP_NAME" not in os.environ:
            print("APP_NAME unset, terminating...")
            exit()
        app_name = os.getenv("APP_NAME")
        while True:
            try:
                requests.get(f"https://{app_name}.herokuapp.com")
            except:
                print("Ping failed, retrying...")
                try:
                    requests.get(f"https://{app_name}.herokuapp.com")
                except:
                    print("Cannot ping app, terminating...")
            sleep(25*60)
