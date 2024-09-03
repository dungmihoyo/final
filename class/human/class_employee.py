
import pypyodbc as odbc
import class_address as class_address
connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=quanlybanhang_khohang;"
    "Trusted_Connection=yes;"
)

class Employee: 
    def __init__(self, ID, name, sex, age, BOD, HOD, phone_number, email, position, City, Area, Commune, Description) :
        self.id = ID 
        self.name = name
        self.sex = sex
        self.age = age
        self.BOD = BOD
        self.HOD = HOD
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.City = City
        self.Area = Area
        self.Commune = Commune
        self.Description = Description
        self.address = class_address.Address(self.ID, self.City, self.Area, self.Commune, self.Description)
    
    def Add_Employee(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = "INSERT INTO Employee (EmployeeID, Name, Age, Sex, BOD, HOD, PhoneNumber, Email, Position) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (int(self.ID), self.name, self.age, self.sex, self.BOD, self.HOD, self.phone_number, self.email, self.position))
        cursor.commit()
        conn.close()
        self.Add_Address_Employee()
        
        
    def Get_EMployee(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"SELECT * FROM Employee WHERE Employee.EmployeeID = {int(self.ID)};"
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        address = self.Get_Address_Employee()
        return data, address
    
    def Set_Customer(self): 
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"""UPDATE Employee SET Name = '{self.name}',
                                        Age = {int(self.age)}, 
                                        Sex = '{self.sex}', 
                                        BOD = '{self.BOD}', 
                                        HOD = '{self.HOD}', 
                                        PhoneNumber = '{self.phone_number}', 
                                        Email = '{self.email}', 
                                        Positon = '{self.position}'
                  WHERE EmployeeID = {int(self.ID)};"""
        cursor.execute(query)
        cursor.commit()
        conn.close()
        self.Set_Address_Employee()

    
    def Remove_Customer(self):
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        query = f"DELETE FROM Employee WHERE EmployeeID= {int(self.ID)};"
        cursor.execute(query)
        cursor.commit()
        conn.close()
        self.Remove_Address_Employee()

        
    def Set_Address_Employee(self) : 
        self.address.Set_Address_Employee()    
    def Add_Address_Employee(self) : 
        self.address.Add_Address_Employee()
        
    def Get_Address_Employee(self) : 
        return self.address.Get_Address_Employee()
    def Remove_Address_Employee(self) : 
        self.address.Remove_Address_Employee()
        
    
    
    