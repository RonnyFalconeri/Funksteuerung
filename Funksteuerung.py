from GUI import *
from Printer import *
from Database import *

class Funksteuerung:
    
    led_state = False 
    
    database = "" 

    def __init__(self):
        log("initialise controller...")
        self.database = Database("Steckdosen_DB.txt")
        gui = GUI(self)
    
    # set n' get -----------------------
    def set_state(self, pState):
        self.led_state = pState
        
    def get_database(self):
        return self.database
