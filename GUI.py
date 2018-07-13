from tkinter import *
from Printer import *
from Settings import *

class GUI:
    
    # Objects
    strg = ""
    settings = ""
    
    # window properties
    window = ""
    height = "200"
    width = "300"
    
    # Labels
    headline_label = ""
    state_label = ""
    
    # Buttons
    settings_button = ""
    on_button = ""
    off_button = ""
    
    
    
    def __init__(self, pStrg):
        log("initialise GUI...")
        
        # object initialising
        self.strg = pStrg
        
        # build window
        self.window = Tk()
        self.window.geometry(self.width+"x"+self.height)
        
        
        # Labels ----------------------------
        self.headline_label = Label(self.window, text="Control Panel")
        self.headline_label.pack(side="top", pady=5)
        
        self.state_label = Label(self.window, text="Turned Off")
        self.state_label.pack(side="top", pady=5)
        
        
        # Buttons ---------------------------
        self.settings_button = Button(self.window, text="Settings")
        self.settings_button.pack(side="top", pady=5)
        self.settings_button.bind("<Button-1>", self.build_settings)
        
        self.on_button = Button(self.window, text="On")
        self.on_button.pack(side="bottom", pady=5)
        self.on_button.bind("<Button-1>", self.turn_on)
        #self.on_button.bind("<1>", self.turn_on)
        
        self.off_button = Button(self.window, text="Off")
        self.off_button.pack(side="bottom", pady=5)
        self.off_button.bind("<Button-1>", self.turn_off)
        #self.off_button.bind("<2>", self.turn_off)


        self.window.mainloop()
    
    
    # action events ------------------------------
    def turn_on(self, event):
        self.state_label.config(text="Turned On") # change label text
        self.strg.set_state(True) # change state in controller

    def turn_off(self, event):
        self.state_label.config(text="Turned Off") # change label text
        self.strg.set_state(False) # change state in controller
    
    def build_settings(self, event):
        self.settings = Settings(self.strg)
