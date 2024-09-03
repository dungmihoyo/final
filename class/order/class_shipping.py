import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)
def Get_ID(): 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"SELECT * FROM Shipping ;"
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

class Shipping: 
    def __init__(self, ShippingID, ShippingMethod, ShippingCost, ShippingAddress):
        self.ShippingID = ShippingID
        self.ShippingMethod = ShippingMethod
        self.ShippingCost = ShippingCost 
        self.ShippingAddress = ShippingAddress
        
    def Set_Shipping(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""UPDATE Shipping SET ShippingMethod = {self.ShippingMethod}, 
                                        ShippingCost = {int(self.TotalPrice)}, 
                                        ShippingAddress = {self.ShippingAddress}
                    WHERE ShippingID = {int(self.ShippingID)};"""
        cursor.execute(query)
        cursor.commit()
        conn.close()
        
    def Get_Shipping(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM Shipping WHERE Shipping.ShippingID = {int(self.ShippingID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    
    def Add_Shipping(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO Shipping (ShippingID, ShippingMethod, ShippingCost, ShippingAddress) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (int(self.ShippingID), self.ShippingMethod, float(self.ShippingCost), self.ShippingAddress))
        cursor.commit()
        conn.close()

    
    def Remove_Shipping(self):
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM Shipping WHERE ShippingID = {int(self.ShippingID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()

        