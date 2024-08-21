import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=Login;"
    "Trusted_Connection=yes;"
)

class Product: 
    def __init__(self, ID, name, categoryid, descriptions):
        self.ID = ID
        self.username = username
        self.password = password
        self.position = position
        self.flag = False 
    
    def set_ID (self, ID): 
        self.ID = ID
    def get_ID (self): 
        return self.ID 
    
    def set_username (self, username): 
        self.username = username
    def get_username (self): 
        return self.username
    
    def set_password (self, password): 
        self.password = password
    def get_password (self): 
        return self.password  
    
    def set_position (self, position): 
        self.position = position
    def get_position (self): 
        return self.position 