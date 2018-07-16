from Printer import *

class Database:
    
    table_column = {"id": 0, "group": 1, "description": 2}
    
    
    # constructor ----------------------
    def __init__(self, pDatabase):
        self.database = pDatabase
        log("create database: "+self.database)
        
    
    # file handling --------------------
    def read_file(self):
        try:
            file = open(self.database,"r")
            data = file.read()
            file.close()
            return data
        except:
            log("Error: Could not read file.")
    
    def write_file(self, id, group, description):
        try:
            file = open(self.database, "w")
            file.write(id+","+group+","+description)
        except:
            log("Error: Could not write file.")
        
    # list handling -------------------
    def get_row(self, index_y):
        data = self.read_file()
        row = data.splitlines()
        return row[index_y]
    
    def get_value(self, value):
        row = self.get_row(0)
        value_list = row.split(",")
        return value_list[self.table_column[value]]
    
    def set_value(self, id, group, description):
        self.write_file(id, group, description)
        