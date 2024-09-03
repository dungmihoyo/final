import pypyodbc as odbc

connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)
conn = odbc.connect(connection_string)
cursor = conn.cursor()
cursor.execute("SELECT * FROM Categories ")
data = cursor.fetchall()
conn.close()
def Find_ID_Category(ID): 
    for i in data : 
        if i[0] == ID : 
            return i
    print(i)
    return None
def Get_ID(): 
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Categories")
    data = cursor.fetchall()
    conn.close()
    id = 0 
    if data ==[]: 
        return id + 1 
    else: 
        for i in data: 
            id = i[0]
    return id+ 1
class Categories: 
    def __init__(self, categoryID, category, category_description) :
        self.categoryID = categoryID
        self.category = category
        self.category_description = category_description
        
    def set_categoryID(self, categoryID):
        self.categoryID = categoryID
    def getget_categoryID(self):
        return self.categoryID

    def set_category(self, category):
        self.category = category
    def getget_categoryID(self):
        return self.category
    
    def set_category_description(self, category_description):
        self.category_description = category_description
    def get_category_description(self):
        return self.category_description
    
    def Check_ID_Category(self): 
        for i in data : 
            if i[0] == self.categoryID: 
                return True
        return False 
    
    def Add_Category(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO Categories (CategoryID, CategoryName, Description) VALUES (?, ?, ?)"
        cursor.execute(query, (int(self.categoryID), self.category, self.category_description))
        cursor.commit()
        conn.close()
    
    def Set_Category(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""UPDATE Categories SET CategoryName = {self.category}, 
                                        Description = {self.category_description}
                  WHERE CategoryID = {int(self.categoryID)};"""
        cursor.execute(query)
        cursor.commit()
        conn.close()
    
    def Get_Category(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM Categories WHERE Categories.CategoryID = {int(self.categoryID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    
    
    def Remove_Category(self):
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM Categories WHERE CategoryID= {int(self.categoryID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()