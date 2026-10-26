# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
#When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program:


import os
import time
from datetime import datetime

target_games = 0
total_games = 0
real_game = True

def click_next():
    global real_game
    lvl_pic = "pearl_next.png"
    try:
        location = pyautogui.locateCenterOnScreen(lvl_pic, confidence=0.9)
        pyautogui.moveTo(location)
        pyautogui.click()
        real_game = True
    except pyautogui.ImageNotFoundException:
        location = False

def click_next2():
    lvl_pic = "pearl_next2.png"
    try:
        location = pyautogui.locateCenterOnScreen(lvl_pic, confidence=0.9)
        pyautogui.moveTo(location)
        pyautogui.click()
    except pyautogui.ImageNotFoundException:
        location = False

def start_click():
    global total_games, real_game
    start_pic = "pearl_start.png"
    try:
        location = pyautogui.locateCenterOnScreen(start_pic, confidence=0.9)
        pyautogui.moveTo(location)
        pyautogui.click()
        #print(real_game, "rael gamee")
        if real_game:
            total_games += 1
            real_game = False
        print(datetime.now(), " : start pressed :=", total_games)
    except pyautogui.ImageNotFoundException:
        location = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("start time ; ", datetime.now())
    #auto()
    #pysimplegui_start()
    #tkinter_start()
    turnon = True
    target_games = 100
    while total_games < (target_games - 1) :
        time.sleep(0.25)
        click_next()
        click_next2()
        start_click()


    print("last round ; ", datetime.now())
    while turnon:
        time.sleep(0.25)
        click_next()
        click_next2()
        start_click()



    print("finished")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
