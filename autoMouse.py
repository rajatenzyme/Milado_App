import pyautogui
import threading
import datetime

screenSize = pyautogui.size()

def moveMouse():
    pyautogui.moveTo(5, screenSize[1], duration = 1)

def clickMouse():
    pyautogui.click()
    main()

def main():
    hour = datetime.datetime.now().hour
    if hour == 17 or hour == 12:
        print("end of day reached")
        quit()
    else:
        threading.Timer(5.0, moveMouse).start()
        threading.Timer(10.0, clickMouse).start()
main()