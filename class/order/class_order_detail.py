import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)
def Get_ID() : 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"SELECT * FROM OrderDetails ;"
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

def Get_Order_Details() : 
    data = [ ] 
    

class Order_Details: 
    def __init__(self, OrderDetailID, ProductID, Quantity, TotalPrice, OrderID):
        self.OrderDetailID = OrderDetailID
        self.ProductID = ProductID
        self.Quantity = Quantity
        self.TotalPrice = TotalPrice
        self.OrderID = OrderID
    
    def Set_Order_Detail(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""UPDATE OrderDetails SET   ProductID = {int(self.ProductID)}, 
                                              Quantity = {int(self.Quantity)}, 
                                              TotalPrice = {float(self.TotalPrice)}
                                              OrderID = {int(self.OrderID)}
                  WHERE OrderDetailID = {int(self.OrderDetailID)};"""
        cursor.execute(query)
        cursor.commit()
        conn.close()
        
    def Get_Order_detail(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM OrderDetails WHERE OrderDetais.OrderDetailID = {int(self.OrderDetailID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    
    def Add_Order_Detail(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO OrderDetails (OrderDetailID, ProductID, TotalPrice, Quantity, OrderID) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (int(self.OrderDetailID), int(self.ProductID), float(self.TotalPrice), int(self.Quantity), int(self.OrderID)))
        cursor.commit()
        conn.close()

    
    def Remove_Order_Detail(self):
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM OrderDetails WHERE OrderDetailID = {int(self.OrderDetailID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()

        
