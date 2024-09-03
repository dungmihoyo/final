from tksheet import Sheet 
import tkinter as tk
import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)
class Sheet_Order: 
    def __init__(self, window):
        self.window = window
        self.screen_height = self.window.winfo_screenheight()
        self.screen_width = self.window.winfo_screenwidth()
    
    def sheet_order(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("""SELECT Products.ProductName, Products.ProductID, Products.ProductName,   FROM OrderDetails, Orders, Invoices, CustomerID  WHERE OrderDetails.OrderID = Orders.OrderID 
                                                                                  AND Shipping.OrderID = Orders.OrderID
                                                                                  AND Invoices.OrderID = Orders.OrderID""")
        data = cursor.fetchall()
        conn.close()