from tksheet import Sheet 
import tkinter as tk
import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)


class Sheet_Customer: 
    def __init__(self, window): 
        self.window = window
        self.screen_height = self.window.winfo_screenheight()
        self.screen_width = self.window.winfo_screenwidth()
        
    def sheet_customer(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("""SELECT Customers.CustomerID, 
                                 Customers.CompanyName,
                                 Customers.Phone,
                                 AddressCustomer.[Tinh/ThanhPho],
                                 AddressCustomer.[Quan/Huyen],
                                 AddressCustomer.[Xa/Phuong/ThiTran],
                                 AddressCustomer.Description
                       FROM Customers, AddressCustomer
                       WHERE Customers.CustomerID = AddressCustomer.CustomerID """)
        data = cursor.fetchall()
        conn.close()
        data = [[i[x] for x in range (len(i))]for i in data]
        if data == []: 
            data = [["" for _ in range(12)] for _ in range(100)]
        else:
            for _ in range (100): 
                data.append(["" for _ in range(7)])
        
        self.sheet_customer = Sheet(self.window, data= data, width= int(self.screen_width*0.55), height= int(self.screen_height*0.7),column_width= 200)
        self.sheet_customer.headers(['Ma khach hang', 'Ten khach hang', 'So dien thoai', 'Tinh/ThanhPho', 'Quan/Huyen', 'Xa/Phuong/ThiTran', 'Description'])
        self.sheet_customer.pack(fill=tk.BOTH, expand=True)
    
    def sheet_customer_search(self, search_value): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT Customers.CustomerID, 
                                 Customers.CompanyName,
                                 Customers.Phone,
                                 AddressCustomer.[Tinh/ThanhPho],
                                 AddressCustomer.[Quan/Huyen],
                                 AddressCustomer.[Xa/Phuong/ThiTran],
                                 AddressCustomer.Description
                       FROM Customers, AddressCustomer
                       WHERE Customers.CustomerID = AddressCustomer.CustomerID AND Customers.CustomerID = {search_value}""")
        data = cursor.fetchall()
        conn.close()
        data = [[i[x] for x in range (len(i))]for i in data]
        if data == []: 
            data = [["" for _ in range(12)] for _ in range(100)]
        else:
            for _ in range (100): 
                data.append(["" for _ in range(7)])
        
        self.sheet_customer = Sheet(self.window, data= data, width= int(self.screen_width*0.55), height= int(self.screen_height*0.7),column_width= 200)
        self.sheet_customer.headers(['Ma khach hang', 'Ten khach hang', 'So dien thoai', 'Tinh/ThanhPho', 'Quan/Huyen', 'Xa/Phuong/ThiTran', 'Description'])
        self.sheet_customer.pack(fill=tk.BOTH, expand=True)
    
    def sheet_customer_filter (self, key): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT Customers.CustomerID, 
                                 Customers.CompanyName,
                                 Customers.Phone,
                                 AddressCustomer.[Tinh/ThanhPho],
                                 AddressCustomer.[Quan/Huyen],
                                 AddressCustomer.[Xa/Phuong/ThiTran],
                                 AddressCustomer.Description
                       FROM Customers, AddressCustomer
                       WHERE Customers.CustomerID = AddressCustomer.CustomerID AND AddressCustomer = {key}""")
        data = cursor.fetchall()
        conn.close()
        data = [[i[x] for x in range (len(i))]for i in data]
        if data == []: 
            data = [["" for _ in range(12)] for _ in range(100)]
        else:
            for _ in range (100): 
                data.append(["" for _ in range(7)])
        
        self.sheet_customer = Sheet(self.window, data= data, width= int(self.screen_width*0.55), height= int(self.screen_height*0.7),column_width= 200)
        self.sheet_customer.headers(['Ma khach hang', 'Ten khach hang', 'So dien thoai', 'Tinh/ThanhPho', 'Quan/Huyen', 'Xa/Phuong/ThiTran', 'Description'])
        self.sheet_customer.pack(fill=tk.BOTH, expand=True)