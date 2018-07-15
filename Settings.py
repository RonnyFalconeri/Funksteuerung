from tkinter import *
from Printer import *

class Settings:
    
    # Objects
    database = ""
    strg = ""
    
    # window properties
    window = ""
    
    # Group Widgets
    one = "0"
    two = "0"
    three = "0"
    four = "1"
    five = "1"
    
    # ID Widgets
    id = "4"
    
    
    def __init__(self, pStrg):
        log("open settings...")
        
        # object initialising
        self.strg = pStrg
        self.database = self.strg.get_database()
        self.window = Tk()
        
        # Group Widgets
        self.one = StringVar()
        self.two = StringVar()
        self.three = StringVar()
        self.four = StringVar()
        self.five = StringVar()
        
        # ID Widgets
        self.id = StringVar()
        
        # Labels ----------------------------
        headline_label = Label(self.window, text="Settings")
        headline_label.grid(row=0, column=7, columnspan=6)
        
        
        # Group Settings --------------------
        
        # row 1
        high_label = Label(self.window, text="1")
        high_label.grid(row=1, column=0)
        
        one_high_radio = Radiobutton(self.window, variable=self.one, value="1")
        one_high_radio.deselect()
        one_high_radio.grid(row=1, column=1)
        
        two_high_radio = Radiobutton(self.window, variable=self.two, value="1")
        two_high_radio.deselect()
        two_high_radio.grid(row=1, column=2)
        
        three_high_radio = Radiobutton(self.window, variable=self.three, value="1")
        three_high_radio.deselect()
        three_high_radio.grid(row=1, column=3)
        
        four_high_radio = Radiobutton(self.window, variable=self.four, value="1")
        four_high_radio.select()
        four_high_radio.grid(row=1, column=4)
        
        five_high_radio = Radiobutton(self.window, variable=self.five, value="1")
        five_high_radio.select()
        five_high_radio.grid(row=1, column=5)
        
        # row 2
        low_label = Label(self.window, text="0")
        low_label.grid(row=2, column=0)
        
        one_low_radio = Radiobutton(self.window, variable=self.one, value="0")
        one_low_radio.select()
        one_low_radio.grid(row=2, column=1)
        
        two_low_radio = Radiobutton(self.window, variable=self.two, value="0")
        two_low_radio.select()
        two_low_radio.grid(row=2, column=2)
        
        three_low_radio = Radiobutton(self.window, variable=self.three, value="0")
        three_low_radio.select()
        three_low_radio.grid(row=2, column=3)
        
        four_low_radio = Radiobutton(self.window, variable=self.four, value="0")
        four_low_radio.deselect()
        four_low_radio.grid(row=2, column=4)
        
        five_low_radio = Radiobutton(self.window, variable=self.five, value="0")
        five_low_radio.deselect()
        five_low_radio.grid(row=2, column=5)
        
        # row 3
        fillergr = Label(self.window, text=" ")
        fillergr.grid(row=3, column=0)
        
        group_label1 = Label(self.window, text="1")
        group_label1.grid(row=3, column=1)
        
        group_label2 = Label(self.window, text="2")
        group_label2.grid(row=3, column=2)
        
        group_label3 = Label(self.window, text="3")
        group_label3.grid(row=3, column=3)
        
        group_label4 = Label(self.window, text="4")
        group_label4.grid(row=3, column=4)
        
        group_label5 = Label(self.window, text="5")
        group_label5.grid(row=3, column=5)
        
        
        # ID Settings --------------------------------
        
        # row 1, 2
        fillerid = Label(self.window, text=" ")
        fillerid.grid(row=1, column=6)
        
        a_radio = Radiobutton(self.window, variable=self.id, value="1")
        a_radio.deselect()
        a_radio.grid(row=1, column=7, rowspan=2)
        
        b_radio = Radiobutton(self.window, variable=self.id, value="2")
        b_radio.deselect()
        b_radio.grid(row=1, column=8, rowspan=2)
        
        c_radio = Radiobutton(self.window, variable=self.id, value="3")
        c_radio.deselect()
        c_radio.grid(row=1, column=9, rowspan=2)
        
        d_radio = Radiobutton(self.window, variable=self.id, value="4")
        d_radio.select()
        d_radio.grid(row=1, column=10, rowspan=2)
        
        e_radio = Radiobutton(self.window, variable=self.id, value="5")
        e_radio.deselect()
        e_radio.grid(row=1, column=11, rowspan=2)
        
        # row 3
        id_label1 = Label(self.window, text="1")
        id_label1.grid(row=3, column=7)
        
        id_label2 = Label(self.window, text="2")
        id_label2.grid(row=3, column=8)
        
        id_label3 = Label(self.window, text="3")
        id_label3.grid(row=3, column=9)
        
        id_label4 = Label(self.window, text="4")
        id_label4.grid(row=3, column=10)
        
        id_label5 = Label(self.window, text="5")
        id_label5.grid(row=3, column=11)
        
        
        # Buttons ---------------------------
        save_button = Button(self.window, text="Save", command = self.save_data)
        save_button.grid(row=1, column=12, columnspan=6, rowspan=2, padx=10)
        
        fillersave1 = Label(self.window, text=" ")
        fillersave1.grid(row=3, column=13, padx=5)
        
        fillersave2 = Label(self.window, text=" ")
        fillersave2.grid(row=3, column=14, padx=5)
        
        fillersave3 = Label(self.window, text=" ")
        fillersave3.grid(row=3, column=15, padx=5)
        
        fillersave4 = Label(self.window, text=" ")
        fillersave4.grid(row=3, column=16, padx=5)
        
        fillersave5 = Label(self.window, text=" ")
        fillersave5.grid(row=3, column=17, padx=5)


        self.window.mainloop()
    
    
    # action events -------------------------
    def save_data(self):
        # group: g1 g2 g3 g4 g5
        g1 = self.one.get()
        g2 = self.two.get()
        g3 = self.three.get()
        g4 = self.four.get()
        g5 = self.five.get()
        group = g1+g2+g3+g4+g5
        id = self.id.get()
        description = "Nachtlampe"
        
        log("save data: "+id+","+group+","+description)
        self.database.set_value(id, group, description)
        
