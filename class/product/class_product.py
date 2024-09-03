import pypyodbc as odbc
import class_category as class_category
import class_supplier as class_supplier
import class_warehouse as class_warehouse 

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)
conn = odbc.connect(connection_string)
cursor = conn.cursor()
cursor.execute("SELECT * FROM Products")
data = cursor.fetchall()
conn.close()
data = [[i[x] for x in range (len(i))]for i in data]

def Find_ID_Product(ID): 
    for i in data : 
        if i[0] == ID : 
            return i
    print(i)
    return None

def Find_Product( ID): 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Products WHERE Products.ProductID = {int(ID)}")
    data = cursor.fetchall()
    conn.close()
    return data

def Update_Product(ID, unitsinstock): 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"""UPDATE Products SET UnitsInStock = {unitsinstock}, 
                        WHERE ProductID = {int(ID)};"""
    cursor.execute(query)
    cursor.commit()
    conn.close()

def Get_ID() : 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    data = cursor.fetchall()
    conn.close()
    id = 0 
    if data ==[]: 
        return id + 1 
    else: 
        for i in data: 
            id = i[0]
    return id+ 1
def Delete_Product(ID): 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"""DELETE FROM Products WHERE ProductID = {ID}"""
    cursor.execute(query)
    cursor.commit() 

class Product: 
    def __init__(self, ID, name, categoryid, supplierid, price, unitsinstock, description, category, category_descriptions, company_name, company_phone):
        self.ID = ID
        self.name = name
        self.categoryid = categoryid
        self.supplierid = supplierid
        self.price = price
        self.unitsinstock = unitsinstock
        self.description = description 
        self.category = class_category.Categories(categoryid, category, category_descriptions)
        self.supplier = class_supplier.Suppliers(supplierid, company_name, company_phone)
        self.flag = False
    
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
    def set_categoryid(self, categoryid):
        self.categoryid = categoryid
    def get_categoryid(self):
        return self.categoryid 
    
    def set_supplierid(self, supplierid):
        self.supplierid = supplierid
    def get_supplierid(self):
        return self.supplierid
    
    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price
    
    def set_unitsinstock(self, unitsinstock):
        self.unitsinstock = unitsinstock
    def get_unitsinstock(self):
        return self.unitsinstock
    
    def set_description(self, description):
        self.description = description
    def get_description(self):
        return self.description 
    
    
    def Add_Product(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = ("INSERT INTO Products (ProductID, ProductName, CategoryID, SupplierID, Price, UnitsInStock, Description) VALUES (?, ?, ?, ?, ?, ?, ?);")
        cursor.execute(query, (int(self.ID), self.name, int(self.categoryid), int(self.supplierid), float(self.price), int(self.unitsinstock) , self.description))
        cursor.commit()
        conn.close()
    

    def Set_Product(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""UPDATE Products SET ProductName = '{self.name}', 
                                        CategoryID = {self.categoryid},  
                                        SupplierID = {self.supplierid}, 
                                        Price = {self.price},
                                        UnitsInStock = {self.unitsinstock}, 
                                        Description = '{self.description}'
                        WHERE ProductID = {int(self.ID)};"""
        cursor.execute(query)
        cursor.commit()
        conn.close()
    
    def Get_Product(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM Products WHERE Products.ProductID = {int(self.ID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    
    def Remove_Product(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM Products WHERE ProductID= {int(self.ID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()
    
    def Find_Product(self): 
        if self.Get_Product() != None: 
            return True
        return False        
    
    
    def Check_ID_Product(self): 
        for i in data: 
            if i[0] == self.ID and i[2] == self.categoryid and i[3] == self.supplierid: 
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()
                cursor.execute(f"UPDATE Products SET UnitsInStock = {self.unitsinstock} WHERE Products.ProductID = {self.ID};")
                cursor.commit()
                conn.close()
                self.flag = True 
                break 
        if self.flag == False: 
            if self.category.Check_ID_Category() == False: 
                self.category.Add_Category() 
            if self.supplier.Check_ID_Supplier() == False:
                self.supplier.Add_Supplier()
            self.Add_Product() 
        
    def Get_WareHouse (self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""SELECT * FROM Warehouses WHERE Warehouses.ProductID = {int(self.ID)}"""
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data 
    
    def Add_New_Product(self): 
        if self.category.Check_ID_Category() == False: 
            self.category.Add_Category() 
        if self.supplier.Check_ID_Supplier() == False:
            self.supplier.Add_Supplier()
        self.Add_Product() 

        
            
