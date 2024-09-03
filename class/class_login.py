import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=Login;"
    "Trusted_Connection=yes;"
)

class Login_Information: 
    def __init__(self, ID, username, password, position):
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
    
    
    def Check_Information(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("Select * from LoginInformation")
        data = cursor.fetchall()
        for i in data : 
            if i[0] == self.ID :
                if i[1] == self.username :
                    if i[2] == self.password : 
                        if i[3] == self.position : 
                            return True
        conn.close()
        return False
    
    def Add_Information(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO LoginInformation (EmployeeID, Username, Password, Position) VALUES ({self.ID}, '{self.username}', '{self.password}', '{self.position}')")
        cursor.commit()
        conn.close()
    
    def Change_Information(self, username, password, position): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE LoginInformation SET Username = '{self.username}', Password = '{self.password}', Position = '{self.position}' WHERE EmployeeID = {self.ID}")
        cursor.commit()
        conn.close()
    
    def Find_profile_employee(self):
        connection_string =(
        "DRIVER={SQL Server};" 
        "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
        "DATABASE=quanlybanhang_khohang;"
        "Trusted_Connection=yes;")    
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()  
        cursor.execute('SELECT * FROM Employee')
        data = cursor.fetchall() 
        query = 'SELECT * FROM AddressEmployee'
        cursor.execute(query)
        data_1 = cursor.fetchall()
        infor = [ ]
        for i in data: 
            if i[0] == self.ID : 
                for w in i : 
                    infor.append(w)
        for i in data_1: 
            if i[0] == self.ID: 
                infor.append(i[1])
                infor.append(i[2])
                infor.append(i[3])
                infor.append(i[4])
        conn.close()
        return infor
    
        
        
    

