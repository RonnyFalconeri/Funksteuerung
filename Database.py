class Database:
    # attributes -----------------------
    database = ""
    
    
    # constructor ----------------------
    def __init__(self, pDatabase):
        print("Created database.")
        self.database = pDatabase
        print("Database: "+self.database)
        
    
    # file handling --------------------
    def read_file(self):
        file = open(self.database,"r")
        data = file.read()
        file.close()
        return data
        
    # list handling -------------------
    def get_row(self, index):
        data = self.read_file()
        row = data.splitlines()
        return row[index]
    
    def get_value(self, index_y, index_x):
        row = self.get_row(index_y)
        value = row.split(",")
        return value[index_x]
        