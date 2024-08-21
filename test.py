import pypyodbc as odbc


connection_string =(
    "DRIVER={SQL Server};" 
    "SERVER=DESKTOP-8P6TMAO\SQLEXPRESS02;"
    "DATABASE=Login;"
    "Trusted_Connection=yes;"
)

conn = odbc.connect(connection_string)
cursor = conn.cursor()
cursor.execute("Select * from LoginInformation")
data = cursor.fetchall()
for i in data : 
    print(i[0])