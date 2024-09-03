import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)

conn = odbc.connect(connection_string)
cursor = conn.cursor()
cursor.execute("SELECT * FROM Suppliers")
data = cursor.fetchall()
conn.close()
def Find_ID_Supplier(ID): 
    for i in data : 
        if i[0] == ID : 
            return i
    print(i)
    return None

def Get_ID() : 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Suppliers")
    data = cursor.fetchall()
    conn.close()
    id = 0 
    if data ==[]: 
        return id + 1 
    else: 
        for i in data: 
            id = i[0]
    return id+ 1


class Suppliers: 
    def __init__(self, supplierID, company_name, company_phome) :
        self.supplierID = supplierID
        self.company_name = company_name
        self.company_phome = company_phome
        
    def set_supplierID(self, supplierID):
        self.supplierIDID = supplierID
    def get_supplierID(self):
        return self.supplierID

    def set_company_name(self, company_name):
        self.company_name = company_name
    def get_company_name(self):
        return self.company_name
    
    def set_company_phone(self, company_phone):
        self.company_phone = company_phone
    def get_company_phone(self):
        return self.company_phome
    
    def Check_ID_Supplier(self): 
        for i in data : 
            if i[0] == self.supplierID: 
                return True
        return False 
    
    def Add_Supplier(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO Suppliers (SupplierID, CompanyName, Phone) VALUES (?, ?, ?)"
        cursor.execute(query, (int(self.supplierID), self.company_name, self.company_phome))
        cursor.commit()
        conn.close()

        
    def Get_Supplier(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM Suppliers WHERE Suoooliers.CustomerID = {int(self.supplierID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    
    def Set_Supplier(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""UPDATE Suppliers SET  CompanyName = {self.company_name}, 
                                        Phone = {self.company_phone}, 
                  WHERE SupplierID = {int(self.supplierID)};"""
        cursor.execute(query)
        cursor.commit()
        conn.close()

    
    def Remove_Supplier(self):
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM Suppliers WHERE SupplierID= {int(self.supplierID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()

