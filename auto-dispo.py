import pyautogui
import time
import re

from Mouse_click import auto_click, calibrate
from Count_down import Countdown

# TODO
# FIX RESETING THE M for the interact_m


def Evaluate_multiple_statements(string, delimiter, Lag):
    listed_statements = string.split(delimiter)
    if listed_statements[0] != '':
        for statement in listed_statements:
            eval(statement)

def Hit_call_button(): # After selecting the F9 adapter
    pyautogui.press('tab', presses=5)
    pyautogui.hotkey('enter')

def main():

    Lag = 1

    """
    Special char guide:
    ? = Dialing, never hit active call
    ! = Call disconnected
    @ = Delete voicemail
    """

    stand_up = 0

    #Calibrate

    print("Calibrating in...")
    Countdown(5)
    SF_x, SF_y = calibrate("Blank space for F9 adapter in SF",sec=5)
    C_x, C_y = calibrate("Top right corner of adaptor", sec=5) #To close the unavailable, no answer, bad number popup
    R_x, R_y = calibrate("Top of reading window",sec=5)

    while True: # Main loop
        while True:
            stand_up += 1
            if stand_up == 10:
                print("Stand up and stretch...")
                stand_up = 0
            Dispo = input("\nPlace dispo: ").lower()
             
            Dispo_options = {
                'ans': 'not dead', 
                'noa' : 'not dead', 
                'dnc':'dead', 
                'alr':'dead', 
                'bad':'dead', 
                'wr':'dead',
                'err':'dead',
                'not':'not dead',
                'b':'not dead',
                'sp':'not dead',
                'imm':'not dead',
                'notq': 'dead-confirm',
                "ass" : "confirm",
                "1" : "not dead",
                "30" : "not dead",
                "60" : "not dead", 
                "ass" : "confirm" #Insert
                }

            Test_dispo = re.sub('[?|!|@]', '', Dispo)

            try:
                Test_dispo = Test_dispo.lower()
            except TypeError:
                pass

            if Test_dispo == "ans":
                eval_str = "pyautogui.hotkey('g', '-', 'm')"
            elif Test_dispo == "noa":
                eval_str = "pyautogui.hotkey('n', 'o', ' ', 'a')"
            elif Test_dispo == "b":
                eval_str = "pyautogui.hotkey('b', 'u')"
            elif Test_dispo == "dnc":
                eval_str = "pyautogui.hotkey('d', 'n', 'c')"
            elif Test_dispo == "alr":
                eval_str = "pyautogui.hotkey('a', 'l', 'r')"
            elif Test_dispo == "bad":
                eval_str = "pyautogui.hotkey('l', 'e', 'a')"
            elif Test_dispo == "wr":
                eval_str = "pyautogui.hotkey('w', 'r')"
            elif Test_dispo == "err":
                eval_str = "pyautogui.hotkey('o', 'r')" 
            elif Test_dispo == "not":
                eval_str = "pyautogui.hotkey('i', 'n', 't', 'e')"
            elif Test_dispo == "sp":
                eval_str = "pyautogui.hotkey('s', 'p', 'e')"
            elif Test_dispo == "imm":
                eval_str = "pyautogui.hotkey('l', 'y')"
            elif Test_dispo == "notq":
                eval_str = "pyautogui.hotkey('n', 'o', 't', ' ', 'q')"
            elif Test_dispo == "1":
                eval_str = "pyautogui.hotkey('1')"
            elif Test_dispo == "30":
                eval_str = "pyautogui.hotkey('3', '0')"
            elif Test_dispo == "60":
                eval_str = "pyautogui.hotkey('6', '0')"
            elif Test_dispo == "ass":
                eval_str = "pyautogui.hotkey('a', 's')"

            if Test_dispo in Dispo_options:
                break
        

        if Dispo.__contains__('!'):
            tab_count = 9
        elif Dispo.__contains__('?'):
            tab_count = 10
        else: #Active call
            tab_count = 16


        eval_deleteMessage = "" #blank is equivalent to pass

        if Dispo.__contains__("@") and not Dispo.__contains__('?'):
            eval_deleteMessage = "pyautogui.press('tab', presses=8)^pyautogui.hotkey('enter')^pyautogui.keyDown('shift')^time.sleep(0.2)^pyautogui.hotkey('8')^time.sleep(0.30)^pyautogui.keyUp('shift')" # Works for all carriers
            tab_count = 8

        #Iniate key presses

        auto_click(C_x, C_y)
        auto_click(SF_x, SF_y) # Click adapter in SF (Stage tabs)

        #Check if any messages to delete
        Evaluate_multiple_statements(eval_deleteMessage, '^', Lag)

        pyautogui.press('tab', tab_count)
        time.sleep(0.05)
        pyautogui.hotkey('enter') #Hit Set Dispo...
        time.sleep(0.05)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('Backspace') #delete anything that might be in the field already
        eval(eval_str) #type the right letters for the dispo
        time.sleep(0.05)
        pyautogui.press('down') 
        pyautogui.hotkey('enter') #Placed Dispo
        
        auto_click(R_x, R_y)

if __name__ == "__main__":
    main()