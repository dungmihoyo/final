import pypyodbc as odbc
import datetime
connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)
def Get_ID() :
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    query = f"SELECT * FROM Invoices;"
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
def Get_Time(): 
    time = datetime.datetime.now()
    return time
class Invoice: 
    def __init__(self, InvoiceID, InvoiceDate, InvoiceAmount, InvoiceMethod): 
        self.InvoiceID = InvoiceID
        self.InvoiceDate = InvoiceDate
        self.InvoiceAmount = InvoiceAmount
        self.InvoiceMethod = InvoiceMethod
    
    def Set_Invoice(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""UPDATE Invoices SET InvoiceMethod = '{self.InvoiceMethod}', 
                                        InvoiceAmount = {float(self.InvoiceAmount)}, 
                                        InvoiceDate = '{self.InvoiceDate}'
                    WHERE InvoiceID = {int(self.InvoiceID)};"""
        cursor.execute(query)
        cursor.commit()
        conn.close()
    
    def Get_Invoice(self) : 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM Invoices  WHERE Invoices.InvoiceID = {int(self.InvoiceID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    
    def Add_Invoice(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO Shipping (InvoiceID, InvoiceMethod, InvoiceAmount, InvoiceDate) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (int(self.InvoiceID), self.InvoiceMethod, float(self.InvoiceAmount), self.InvoiceDate))
        cursor.commit()
        conn.close()
    
    def Remove_Invoice(self) : 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM Invoices WHERE InvoiceID= {int(self.InvoiceID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()