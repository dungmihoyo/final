from tksheet import Sheet 
import tkinter as tk
import pypyodbc as odbc


connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)


def Get_Order(): 
    data = [ ] 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = """ SELECT
                OrderDetails.OrderDetailID
                Products.ProductName,
                Products.ProductID,
                 
                Products.Price,
                OrderDetails.Quantity
            FROM
                Products
            LEFT JOIN OrderDetails
                ON Products.ProductID = OrderDetails.ProductID"""
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    

def Get_ID():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"SELECT * FROM Orders;"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    id = 0
    if data == [ ]:
        return id + 1 
    else: 
       for i in data : 
           id = int(i[0])
    return id + 1 

class Order: 
    def __init__(self, OrderID, CustomerID, EmployeeID,  InvoiceID, ShippingID, OrderDate) :
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.EmployeeID = EmployeeID
        self.InvoiceID = InvoiceID 
        self.ShippingID = ShippingID
        self.OrderDate = OrderDate
    def Set_Order(self) : 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""UPDATE Orders SET   CustomerID = {int(self.CustomerID)}, 
                                        EmployeeID = {int(self.EmployeeID)}, 
                                        InvoiceID = {int(self.InvoiceID)}, 
                                        ShippingID = {int(self.ShippingID)}
                                        OrderDate ='{self.OrderDate}'
                    WHERE OrderID = {int(self.OrderID)};"""
        cursor.execute(query)
        cursor.commit()
        conn.close()
    
    def Get_Order(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM Orders  WHERE Orders.OrderID = {int(self.OrderID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    
    def Add_Order(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO Orders (OrderID, CustomerID, EmployeeID, InvoiceID, ShippingID, OrderDate) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (int(self.OrderID), int(self.CustomerID), int(self.EmployeeID), int(self.InvoiceID), int(self.ShippingID), self.OrderDate))
        cursor.commit()
        conn.close()
    
    def Remove_Order(self) : 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM Orders WHERE OrderID= {int(self.OrderID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()