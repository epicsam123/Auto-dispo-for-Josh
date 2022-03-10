import pyautogui

from Count_down import Countdown

def auto_click(x, y):
    save_x, save_y = pyautogui.position()   
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.moveTo(save_x, save_y)


def calibrate(message, sec):
    """
    Parameters:
    Sec - Time to countdown
    """
    print(f"Calibrating {message} in...")
    Countdown(sec)
    x, y = pyautogui.position() 
    return x, y
