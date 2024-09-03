import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)

class Address: 
    def __init__(self, ID, City, Area, Commune, Desciption):
        self.ID = ID
        self.City = City
        self.Area = Area
        self.Commune = Commune
        self.Desciption = Desciption
    
    def Add_Address_Customer(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO AddressCustomer (CustomerID, [Tinh/ThanhPho], [Quan/Huyen], [Xa/Phuong/ThiTran], Description) VALUES (?, ?, ?, ?, ?);"
        cursor.execute(query, (int(self.ID), self.City, self.Area, self.Commune, self.Desciption))
        cursor.commit()
        conn.close()
    
    def Add_Address_Employee(self):
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO AddressEmployee (EmployeeID, [Tinh/ThanhPho], [Quan/Huyen], [Xa/Phuong/ThiTran], Description) VALUES (?, ?, ?, ?, ?);"
        cursor.execute(query, (int(self.ID), self.City, self.Area, self.Commune, self.Desciption))
        cursor.commit()
        conn.close()
    
    def Get_Address_Customer(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM AddressCustomer WHERE AddressCustomer.CustomerID = {int(self.ID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data 
    
    def Get_Address_Employee(self):
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM AddressEmployee WHERE AddressEmployee.EmployeeID = {int(self.ID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data 
    
    def Set_Address_Employee(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"UPDATE AddressEmployee SET [Tinh/ThanhPho] = {self.City}, \
                                             [Quan/Huyen] = {self.Area}, \
                                             [Xa/Phuong/ThiTran] = {self.Commune},\
                                             Description = {self.Desciption}\
                  WHERE EmployeeID = {int(self.ID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()
    def Set_Address_Customer(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"UPDATE AddressCustomer SET [Tinh/ThanhPho] = {self.City}, \
                                             [Quan/Huyen] = {self.Area}, \
                                             [Xa/Phuong/ThiTran] = {self.Commune},\
                                             Description = {self.Desciption}\
                  WHERE CustomerID = {int(self.ID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()
    
    def Remove_Address_Employee(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM AddressEmployee WHERE EmployeeID= {int(self.ID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        
    def Remove_Address_Customer(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM AddressCustomer WHERE CustomerID= {int(self.ID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()