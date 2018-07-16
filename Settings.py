from tkinter import *
from Printer import *

class Settings:
    
    # label
    headline_font = ("Arial", 25)
    
    def __init__(self, strg, gui):
        log("open settings...")
        
        # object initialising
        self.strg = strg
        self.gui = gui
        self.database = self.strg.get_database()
        self.window = Tk()
        
        # Input Variables
        self.one = StringVar()
        self.two = StringVar()
        self.three = StringVar()
        self.four = StringVar()
        self.five = StringVar()
        self.id = StringVar()
        self.description = StringVar()        
        
        # Labels ----------------------------
        headline_label = Label(self.window, text="Settings", font=self.headline_font)
        headline_label.grid(row=0, column=0, columnspan=12)
        
        
        # Group Settings --------------------
        
        # Group Radios High
        high_label = Label(self.window, text="1")
        high_label.grid(row=1, column=0)
        
        one_high_radio = Radiobutton(self.window, variable=self.one, value="1")
        self.init_radio_group_high(one_high_radio,0)
        one_high_radio.grid(row=1, column=1)
        
        two_high_radio = Radiobutton(self.window, variable=self.two, value="1")
        self.init_radio_group_high(two_high_radio,1)
        two_high_radio.grid(row=1, column=2)
        
        three_high_radio = Radiobutton(self.window, variable=self.three, value="1")
        self.init_radio_group_high(three_high_radio,2)
        three_high_radio.grid(row=1, column=3)
        
        four_high_radio = Radiobutton(self.window, variable=self.four, value="1")
        self.init_radio_group_high(four_high_radio,3)
        four_high_radio.grid(row=1, column=4)
        
        five_high_radio = Radiobutton(self.window, variable=self.five, value="1")
        self.init_radio_group_high(five_high_radio,4)
        five_high_radio.grid(row=1, column=5)
        
        # Group Radios Low
        low_label = Label(self.window, text="0")
        low_label.grid(row=2, column=0)
        
        one_low_radio = Radiobutton(self.window, variable=self.one, value="0")
        self.init_radio_group_low(one_low_radio,0)
        one_low_radio.grid(row=2, column=1)
        
        two_low_radio = Radiobutton(self.window, variable=self.two, value="0")
        self.init_radio_group_low(two_low_radio,1)
        two_low_radio.grid(row=2, column=2)
        
        three_low_radio = Radiobutton(self.window, variable=self.three, value="0")
        self.init_radio_group_low(three_low_radio,2)
        three_low_radio.grid(row=2, column=3)
        
        four_low_radio = Radiobutton(self.window, variable=self.four, value="0")
        self.init_radio_group_low(four_low_radio,3)
        four_low_radio.grid(row=2, column=4)
        
        five_low_radio = Radiobutton(self.window, variable=self.five, value="0")
        self.init_radio_group_low(five_low_radio,4)
        five_low_radio.grid(row=2, column=5)
        
        # Group Labels
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
        
        # ID Radios
        fillerid = Label(self.window, text=" ")
        fillerid.grid(row=1, column=6)
        
        a_radio = Radiobutton(self.window, variable=self.id, value="1")
        self.init_radio_id(a_radio, 0)
        a_radio.grid(row=1, column=7, rowspan=2)
        
        b_radio = Radiobutton(self.window, variable=self.id, value="2")
        self.init_radio_id(b_radio, 1)
        b_radio.grid(row=1, column=8, rowspan=2)
        
        c_radio = Radiobutton(self.window, variable=self.id, value="3")
        self.init_radio_id(c_radio, 2)
        c_radio.grid(row=1, column=9, rowspan=2)
        
        d_radio = Radiobutton(self.window, variable=self.id, value="4")
        self.init_radio_id(d_radio, 3)
        d_radio.grid(row=1, column=10, rowspan=2)
        
        e_radio = Radiobutton(self.window, variable=self.id, value="5")
        self.init_radio_id(e_radio, 4)
        e_radio.grid(row=1, column=11, rowspan=2)
        
        # ID Labels
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
        
        
        # Text Input ------------------------
        self.text_input = Entry(self.window, textvariable=self.description)
        self.text_input.grid(row=1, column=12, columnspan=6)
        
        description_label = Label(self.window, text="Description")
        description_label.grid(row=2, column=12, columnspan=6)
        
        
        # Button ---------------------------
        save_button = Button(self.window, text="Save", command = self.save_data)
        save_button.grid(row=1, column=19, columnspan=6, rowspan=2, padx=10)

        self.window.mainloop()
    
    
    # action events -------------------------
    def save_data(self):
        g1 = self.one.get()
        g2 = self.two.get()
        g3 = self.three.get()
        g4 = self.four.get()
        g5 = self.five.get()
        
        group = g1+g2+g3+g4+g5
        
        id = self.id.get()
        
        description = self.description.get()
        if description is "":
            description = "DEFAULT"
        
        log("save data: "+str(id)+","+str(group)+","+str(description))
        self.database.set_value(id, group, description)
        self.gui.refresh_description()
    
    def init_radio_group_high(self, radiobutton, index):
        group = list(self.database.get_value("group"))
        state = group[index]
        if state is "0":
            radiobutton.deselect()
        elif state is "1":
            radiobutton.select()
    
    def init_radio_group_low(self, radiobutton, index):
        group = list(self.database.get_value("group"))
        state = group[index]
        if state is "0":
            radiobutton.select()
        elif state is "1":
            radiobutton.deselect()
        
    def init_radio_id(self, radiobutton, index):
        id = self.database.get_value("id")
        radiobutton.deselect
        if id is "1" and index == 0:
            radiobutton.select()
        elif id is "2" and index == 1:
            radiobutton.select()
        elif id is "3" and index == 2:
            radiobutton.select()
        elif id is "4" and index == 3:
            radiobutton.select()
        elif id is "5" and index == 4:
            radiobutton.select()
            
