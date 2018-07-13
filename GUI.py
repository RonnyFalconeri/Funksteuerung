from tkinter import *
from Printer import *

class GUI:
    
    # window properties
    window = ""
    height = "200"
    width = "300"
    
    # labels
    headline_label = ""
    state_label = ""
    
    # buttons
    on_button = ""
    off_button = ""
    
    
    
    def __init__(self):
        log("Hallo log")
        window = Tk()
        window.geometry(self.width+"x"+self.height)


        window.mainloop()
    
    
    # action events ------------------------------
    def turnOn(self):
        global state
        changeLabelText(bottomLabel, "Turned On")
        state = True

    def turnOff(self):
        global state
        changeLabelText(bottomLabel, "Turned Off")
        state = False
