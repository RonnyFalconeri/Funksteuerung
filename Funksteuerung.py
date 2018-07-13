from tkinter import *
from GUI import *

state = False

### GUI modification ---------------------------
##def changeLabelText(pLabel, pText):
##    pLabel.config(text = pText)

# action events ------------------------------
##def turnOn():
##    global state
##    changeLabelText(bottomLabel, "Turned On")
##    state = True
##
##def turnOff():
##    global state
##    changeLabelText(bottomLabel, "Turned Off")
##    state = False
    
def save_data():
    print("saving data and closing...")
    
def open_settings():    
    settings = Tk()
    settings.geometry("250x150")
    
    top_label = Label(settings, text = "Settings")
    top_label.pack(pady = 5)
    
    save_button = Button(settings, text = "Save", command = save_data)
    save_button.pack(side = "right", pady = 5)
    
    settings.mainloop()
    
gui = GUI()
# window build --------------------------------
##window = Tk()
##window.geometry("300x200")
##
### top label
##topLabel = Label(window, text = "Funksteuerung")
##topLabel.pack(pady = 5)
##
### bottom label
##bottomLabel = Label(window, text = "Turned Off")
##bottomLabel.pack(pady = 5)
##
##
### settings button
##settingsButton = Button(window, text = "Settings", command = open_settings)
##settingsButton.pack(side = "top", pady = 5)
##
### buttonOn
##topButton = Button(window, text = "Switch On", command = turnOn)
##topButton.pack(side = "left", pady = 5)
##
### buttonOff
##topButton = Button(window, text = "Switch Off", command = turnOff)
##topButton.pack(side = "right", pady = 5)
##
##window.mainloop()