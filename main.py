# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
pyautogui.PAUSE = 1.0
pyautogui.FAILSAFE = True
#When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program:


import os
import PySimpleGUI as sg

def auto():
    print("position :",pyautogui.position())
    pyautogui.moveTo(10, 10)  #, duration=num_seconds)
    print("position :", pyautogui.position())
    print("screen size :", pyautogui.size())

    file_path = "pycharm_taskbar.png"

    if os.path.isfile(file_path):
        print("File exists")
    else:
        print("File does not exist")

    try:
        location = pyautogui.locateCenterOnScreen(file_path, confidence=0.9)
        print(location)
        print(location[0])
    except pyautogui.ImageNotFoundException:
        location = None
        print(location)
        #print("Image not found on screen.")

    #ishere = pyautogui.locateOnScreen('pycharm_taskbar.png')



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



def pysimplegui_start():
    import PySimpleGUI as sg

    # Define the layout with a single button
    layout = [[sg.Button('Click Me')]]

    # Create the window
    window = sg.Window('My First Window', layout)

    # Event loop to handle button clicks
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Click Me':
            break

    window.close()

def tkinter_start():
    import tkinter as tk

    # 1. Create the main window
    root = tk.Tk()
    root.title("My First GUI")
    root.geometry("800x200")

    # 2. Add widgets
    label = tk.Label(root, text="Hello, World!")
    label.pack(pady=20)

    button = tk.Button(root, text="Click Me", command=lambda: print("Clicked"))
    button.pack()

    # 3. Start the event loop
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    auto()
    #pysimplegui_start()
    #tkinter_start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
