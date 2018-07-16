from Printer import *
from GUI import *
from Funker import *
from Database import *

class Funksteuerung:
    
    led_state = False 

    def __init__(self):
        log("initialise controller...")
        
        self.database = Database("Steckdosen_DB.txt")
        self.funker = Funker()
        self.gui = GUI(self)
    
    # LED control ----------------------
    def turn_on(self):
        id = self.database.get_value("id")
        group = self.database.get_value("group")
        self.funker.turn_on(id, group)
        
    def turn_off(self):
        id = self.database.get_value("id")
        group = self.database.get_value("group")
        self.funker.turn_off(id, group)
    
    # set n' get -----------------------
    def set_state(self, pState):
        self.led_state = pState
        
    def get_database(self):
        return self.database
