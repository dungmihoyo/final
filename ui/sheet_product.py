from tksheet import Sheet 
import tkinter as tk
import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)


class Sheet_Product: 
    def __init__(self, window): 
        self.window = window
        self.screen_height = self.window.winfo_screenheight()
        self.screen_width = self.window.winfo_screenwidth()
        
    
    def sheet_product(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products, Categories, Suppliers WHERE Products.CategoryID = Categories.CategoryID AND Products.SupplierID = Suppliers.SupplierID")
        data = cursor.fetchall()
        conn.close()
        data = [[i[x] for x in range (len(i))]for i in data]
        if data == []: 
            data = [["" for _ in range(12)] for _ in range(100)]
        else:
            for _ in range (100): 
                data.append(["" for _ in range(12)])
            for i in data: 
                i.pop(10)
                i.pop(7)
        
        self.sheet_product = Sheet(self.window, data= data, width= int(self.screen_width*0.8), height= int(self.screen_height*0.75),column_width= 200)
        self.sheet_product.headers(['ID', 'Name', 'CategoryID', 'SupplierID', 'Price', 'Units in stock', 'Description', 'Catergory', 'Category_Description', 'Company_Supplied', 'Phone_Number'])
        self.sheet_product.pack(fill=tk.BOTH, expand=True)
    
    
    def sheet_product_units(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products, Categories, Suppliers WHERE Products.CategoryID = Categories.CategoryID AND Products.SupplierID = Suppliers.SupplierID AND Products.UnitsInStock <= 10")
        data = cursor.fetchall()
        conn.close()
        data = [[i[x] for x in range (len(i))]for i in data]
        if data == []: 
            data = [["" for _ in range(12)] for _ in range(100)]
        else:
            for _ in range (100): 
                data.append(["" for _ in range(12)])
            for i in data: 
                i.pop(10)
                i.pop(7)
        
        self.sheet_product_units = Sheet(self.window, data= data, width= int(self.screen_width*0.8), height= int(self.screen_height*0.75), column_width= 200)
        self.sheet_product_units.headers(['ID', 'Name', 'CategoryID', 'SupplierID', 'Price', 'Units in stock', 'Description', 'Catergory', 'Category_Description', 'Company_Supplied', 'Phone_Number'])
        self.sheet_product_units.pack(fill=tk.BOTH, expand=True)
    
    def sheet_product_units_zero(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products, Categories, Suppliers WHERE Products.CategoryID = Categories.CategoryID AND Products.SupplierID = Suppliers.SupplierID AND Products.UnitsInStock = 0")
        data = cursor.fetchall()
        conn.close()
        data = [[i[x] for x in range (len(i))]for i in data]
        if data == []: 
            data = [["" for _ in range(12)] for _ in range(100)]
        else:
            for _ in range (100): 
                data.append(["" for _ in range(12)])
            for i in data: 
                i.pop(10)
                i.pop(7)
        self.sheet_product_units_zero = Sheet(self.window, data= data, width= int(self.screen_width*0.8), height= int(self.screen_height*0.75), column_width= 200)
        self.sheet_product_units_zero.headers(['ID', 'Name', 'CategoryID', 'SupplierID', 'Price', 'Units in stock', 'Description', 'Catergory', 'Catergory_Description', 'Company_Supplied', 'PhoneNumber'])
        self.sheet_product_units_zero.pack(fill=tk.BOTH, expand=True)
    
    def sheet_search_product(self, id): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Products, Categories, Suppliers WHERE Products.CategoryID = Categories.CategoryID AND Products.SupplierID = Suppliers.SupplierID AND Products.ProductID = '{id}'")
        data = cursor.fetchall()
        conn.close()
        data = [[i[x] for x in range (len(i))]for i in data]
        if data == []: 
            data = [["" for _ in range(12)] for _ in range(100)]
        else:
            for _ in range (100): 
                data.append(["" for _ in range(12)])
            for i in data: 
                i.pop(10)
                i.pop(7)

        self.sheet_product_search = Sheet(self.window, data= data, width= int(self.screen_width*0.8), height= int(self.screen_height*0.75), column_width= 200)
        self.sheet_product_search.headers(['ID', 'Name', 'CategoryID', 'SupplierID', 'Price', 'Units in stock', 'Description', 'Catergory', 'Category_Description', 'Company_Supplied', 'PhoneNumber'])
        self.sheet_product_search.pack(fill=tk.BOTH, expand=True)
    
    