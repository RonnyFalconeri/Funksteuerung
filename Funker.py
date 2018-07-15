from Printer import *
import os

class Funker:
    
    def __init__(self):
        log("initialise Funker...")
    
    
    # LED switches ------------------------
    def turn_on(self, id, group):
        try:
            log("funker on:  "+group+" "+id+" 1")
            os.System("sudo /home/pi/rcswitch-pi/ ./send "+group+" "+id+" 1")
        except:
            log("Error: Could not send data.")
        
    def turn_off(self, id, group):
        try:
            log("funker off: "+group+" "+id+" 0")
            os.System("sudo /home/pi/rcswitch-pi/ ./send "+group+" "+id+" 0")
        except:
            log("Error: Could not send data.")