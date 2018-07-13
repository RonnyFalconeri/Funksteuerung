from tkinter import *
from Printer import *

class Settings:
    
    # Objects
    database = ""
    strg = ""
    
    # window properties
    window = ""
    height = "180"
    width = "280"
    
    # Labels
    headline_label = ""
    
    # Buttons
    save_button = ""
    
    
    def __init__(self, pStrg):
        log("open settings...")
        
        # object initialising
        self.strg = pStrg
        self.database = self.strg.get_database()
        
        self.window = Tk()
        self.window.geometry(self.width+"x"+self.height)
        
        
        # Labels ----------------------------
        self.headline_label = Label(self.window, text="Settings")
        self.headline_label.pack(side="top", pady=5)
        
        
        # Buttons ---------------------------
        self.save_button = Button(self.window, text="Save", command = self.save_data)
        self.save_button.pack(side="right", pady=5)


        self.window.mainloop()
    
    # action events -------------------------
    def save_data(self):
        log("save data...")
        
