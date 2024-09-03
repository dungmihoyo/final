import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)
class WareHouse: 
    def __init__(self, WareHouseID, WareHouseName, Location, Capacity, ProductID) :
        self.WareHouseID = WareHouseID
        self.WareHouseName = WareHouseName
        self.Location = Location
        self.Capacity = Capacity 
        self.ProductID = ProductID
        
    def Set_WareHouse(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""UPDATE Warehouses SET WarehouseName = {self.WareHouseName}, 
                                        Location = {self.Location}, 
                                        Capacity = {int(self.Capacity)}. 
                                        ProductID = {int(self.ProductID)}
                  WHERE WarehouseID = {int(self.WarehouseID)};"""
        cursor.execute(query)
        cursor.commit()
        conn.close()  
          
    def Get_WareHouse(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM Warehouses WHERE Warehouses.WareouseID = {int(self.WarehouseID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()   
        return data 
        
        
    def Add_Warehouse(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO Warehouses (WareHouseID, WarehouseName, Location, Capacity, ProdutID) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (int(self.WareHouseID), self.WareHouseName, self.Location, int(self.Capacity), int(self.ProductID)))
        cursor.commit()
        conn.close()
        
    def Remove_Warehouse(self):
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM Warehouses WHERE WarehouseID= {int(self.WarehouseID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()
    
    
    