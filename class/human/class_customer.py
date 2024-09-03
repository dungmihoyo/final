import pypyodbc as odbc
import class_address as class_address
connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)


def Find_Cus_Add (ID):
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"""SELECT Customers.CustomerID, 
                       Customers.CompanyName,
                       Customers.Phone,
                       AddressCustomer.[Tinh/ThanhPho], 
                       AddressCustomer.[Quan/Huyen], 
                       AddressCustomer.[Xa/Phuong/ThiTran],
                       AddressCustomer.Description
                       FROM Customers , AddressCustomer 
                       WHERE Customers.CustomerID = {int(ID)} AND Customers.CustomerID = AddressCustomer.CustomerID;"""
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data


def Find_Customer(ID): 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"SELECT * FROM Customers WHERE Customers.CustomerID = {int(ID)};"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    # address = class_address.Get_Address_Customer()
    return data

def Get_ID() : 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"SELECT * FROM Customers ;"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    count = 0 
    if data == [ ] : 
        return count + 1 
    else: 
        for i in data: 
            count = i[0]
    return count + 1 

def Delete_Customer(ID): 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"""DELETE FROM AddressCustomer WHERE CustomerID = {ID}"""
    cursor.execute(query)
    cursor.commit() 
    query = f"""DELETE FROM Customers WHERE CustomerID = {ID}"""
    cursor.execute(query)
    cursor.commit() 
    conn.close()
    
class Customer: 
    def __init__(self, CustomerID, CompanyName, Phone, City, Area, Commune, Description):
        self.CustomerID = CustomerID
        self.CompanyName = CompanyName
        self.Phone = Phone 
        self.City = City
        self.Area = Area
        self.Commune = Commune
        self.Description = Description
        self.address = class_address.Address(self.CustomerID, self.City, self.Area, self.Commune, self.Description)
    
    def Add_Customer(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO Customers (CustomerID, CompanyName, Phone) VALUES (?, ?, ?)"
        cursor.execute(query, (int(self.CustomerID), self.CompanyName, self.Phone))
        cursor.commit()
        conn.close()
        self.Add_Address_Customer()
        
        
    def Get_Customer(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM Customers WHERE Customers.CustomerID = {int(self.CustomerID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        address = self.Get_Address_Customer()
        return data, address
    
    def Set_Customer(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"UPDATE Customers SET  CompanyName = {self.CompanyName}, \
                                        Phone = {self.Phone}, \
                  WHERE CustomerID = {int(self.CustomerID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        self.Set_Address_Customer()
        # self.address.Set_Address_Customer()
    
    def Remove_Customer(self):
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM Customers WHERE CustomerID= {int(self.CustomerID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        self.Remove_Address_Customer()
        # self.address.Remove_Address_Customer()
        
    def Set_Address_Customer(self) : 
        self.address.Set_Address_Customer()    
    def Add_Address_Customer(self) : 
        self.address.Add_Address_Customer()
        
    def Get_Address_Customer(self) : 
        return self.address.Get_Address_Customer()
    def Remove_Address_Customer(self) : 
        self.address.Remove_Address_Customer()
    