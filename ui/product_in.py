import tkinter as tk
import sys 
sys.path.append('./class/product')
import class_product
import class_category
import class_supplier
sys.path.append('./class/human')
import class_customer
class Product_In_Out: 
    def __init__(self, root): 
        self.root = root
        # self.root.title('cua so chinh')
        
        self.screen_height = self.root.winfo_screenheight()
        self.screen_width = self.root.winfo_screenwidth()
        # self.root.geometry(f"{int(self.screen_width*0.5)}x{int(self.screen_height*0.6)}")
        
        self.ID = tk.StringVar()
        self.name = tk.StringVar()
        self.categoryid = tk.StringVar()
        self.supplyid = tk.StringVar()
        self.price = tk.StringVar()
        self.unitsinstock = tk.StringVar()
        self.unitssupply = tk.StringVar()
        self.description = tk.StringVar()
        self.category = tk.StringVar()
        self.category_description = tk.StringVar()
        self.company_name = tk.StringVar()
        self.company_phone = tk.StringVar()
        
        self.quantity = tk.StringVar()
        self.customerID = tk.StringVar() 
        self.employeeID = tk.StringVar() 
        self.shippingID = tk.StringVar()
        self.order_detailID = tk.StringVar()
        self.invoiceID = tk.StringVar()
        
        
        
        
        # tk.Button(self.root, text="Nhap hang", command=self.create_window_product_in).pack(pady=20)
        # tk.Button(self.root, text="Xuat hang", command=self.create_window_product_out).pack(pady=20)
        
        # self.root.mainloop()

    def create_window_product_in(self): 
        self.window_1= tk.Toplevel(self.root)
        self.window_1.geometry(f"{int(self.screen_width*0.5)}x{int(self.screen_height*0.6)}")
        self.window_1.title('Phieu nhap hang')
        self.canvas_in = tk.Canvas(self.window_1, width=int(self.screen_width*0.5), height= int(self.screen_height*0.6), borderwidth= 0, highlightthickness= 0, background= 'white') 
        
        self.frame_search = tk.Frame(self.canvas_in, background='white', width= int(self.screen_width*0.5))
        self.frame_product_form = tk.Frame(self.canvas_in, background='white')
        self.frame_product_entry = tk.Frame(self.canvas_in, background='white')
        self.frame_supplier_form = tk.Frame(self.canvas_in, background='white')
        self.frame_supplier_entry = tk.Frame(self.canvas_in, background='white')
        self.frame_category_form = tk.Frame(self.canvas_in, background='white') 
        self.frame_category_entry = tk.Frame(self.canvas_in, background='white')
        self.frame_units_form = tk.Frame(self.canvas_in, background='white') 
        self.frame_units_entry = tk.Frame(self.canvas_in, background='white')
        self.frame_submit = tk.Frame(self.canvas_in, background='white')
        
        tk.Button(self.frame_search, text= 'Tim kiem:  ', font=('Arial', 15) , background='white', command= self.get_product_information).pack(side= tk.LEFT)
        tk.Entry(self.frame_search, textvariable= self.ID, font=('Arial', 15), width= 50, background='white').pack(side= tk.RIGHT)
        
        tk.Label(self.frame_product_form, text= 'Thong tin san pham', font=('Arial',15), background='white').pack()
        tk.Label(self.frame_product_form, text='ID: ', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_product_entry, textvariable=self.ID, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_product_form, text='Name: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_product_entry, textvariable=self.name, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_product_form, text='Price: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_product_entry, textvariable=self.price, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_product_form, text='Description: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_product_entry, textvariable=self.description, font=('Arial', 15), background='white').pack(pady= 5)
        
        tk.Label(self.frame_category_form, text= 'Thong tin loai', font=('Arial',15), background='white').pack(pady=5)
        tk.Button(self.frame_category_entry, text= 'Tim kiem', font=('Arial',15), background='white', command= self.get_category_information).pack(pady=5)
        tk.Label(self.frame_category_form, text='Category_ID: ', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_category_entry, textvariable=self.categoryid, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_category_form, text='Category: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_category_entry, textvariable=self.category, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_category_form, text='Description: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_category_entry, textvariable=self.category_description, font=('Arial', 15), background='white').pack(pady= 5)
        
        tk.Label(self.frame_supplier_form, text= 'Thong tin nha cung cap', font=('Arial',15), background='white').pack(pady=5)
        tk.Button(self.frame_supplier_entry, text= 'Tim kiem', font=('Arial',15), background='white', command= self.get_supplier_information).pack(pady=5)
        tk.Label(self.frame_supplier_form, text='Supplier_ID: ', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_supplier_entry, textvariable=self.supplyid, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_supplier_form, text='Company_Name: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_supplier_entry, textvariable=self.company_name, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_supplier_form, text='Company_Phone: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_supplier_entry, textvariable=self.company_phone, font=('Arial', 15), background='white').pack(pady= 5)
        
        tk.Label(self.frame_units_form, text= 'Thong tin so luong ', font=('Arial',15), background='white').pack(pady=5)
        tk.Label(self.frame_units_form, text='Units in stock:', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_units_entry, textvariable=self.unitsinstock, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_units_form, text='Units supply: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_units_entry, textvariable=self.unitssupply, font=('Arial', 15), background='white').pack(pady= 5)
        
        tk.Button(self.frame_submit, text= 'Nhap hang', font = ('Arial', 15), background='white', command=self.update_information).pack(pady=5)
        
        self.canvas_in.pack()
        self.canvas_in.create_window(int(self.screen_width *0.25), int(self.screen_height*0.02), window= self.frame_search, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.08), int(self.screen_height*0.1), window= self.frame_product_form, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.18), int(self.screen_height*0.13), window= self.frame_product_entry, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.3), int(self.screen_height*0.1), window= self.frame_category_form, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.4), int(self.screen_height*0.1), window= self.frame_category_entry, anchor= tk.N)
        
        self.canvas_in.create_line(int(self.screen_width*0.03), int(self.screen_height*0.28), int(self.screen_width*0.45), int(self.screen_height*0.28))
        
        self.canvas_in.create_window(int(self.screen_width *0.08), int(self.screen_height*0.3), window= self.frame_supplier_form, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.18), int(self.screen_height*0.3), window= self.frame_supplier_entry, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.3), int(self.screen_height*0.3), window= self.frame_units_form, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.4), int(self.screen_height*0.34), window= self.frame_units_entry, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.35), int(self.screen_height*0.45), window= self.frame_submit, anchor= tk.N)
        
    def get_product_information(self): 
        ID_value = int(self.ID.get())
        product_information = class_product.Find_ID_Product(ID_value)

        
        if product_information != None :
            self.name.set(f'{product_information[1]}')
            self.categoryid.set(f'{product_information[2]}')
            self.supplyid.set(f'{product_information[3]}')
            self.price.set(f'{product_information[4]}')
            self.unitsinstock.set(f'{product_information[5]}')
            self.description.set(f'{product_information[6]}')
            self.get_category_information()
            self.get_supplier_information()
    def get_category_information(self): 
        ID_value = int(self.categoryid.get())
        category_information = class_category.Find_ID_Category(ID_value)  
        self.category.set(f'{category_information[1]}')
        self.category_description.set(f'{category_information[2]}')
        
    def get_supplier_information(self): 
        ID_value = int(self.supplyid.get())
        supplier_information = class_supplier.Find_ID_Supplier(ID_value)
        self.company_name.set(f'{supplier_information[1]}')
        self.company_phone.set(f'{supplier_information[2]}')
    
    def update_information(self): 
        ID_value = self.ID.get()
        name_value = self.name.get()
        category_id_value = self.categoryid.get()
        supplier_id_value = self.supplyid.get()
        price_value = self.price.get()
        units_stock_value = self.unitsinstock.get()
        unit_supply_value =  self.unitssupply.get()
        description_value = self.description.get()
        category_value = self.category.get()
        category_description_value = self.category_description.get()
        company_name_value = self.company_name.get()
        company_phone_value = self.company_phone.get()
        units_stock_value = int(units_stock_value) + int(unit_supply_value)
        
        Product = class_product.Product(int(ID_value), 
                                        name_value, 
                                        int(category_id_value), 
                                        int(supplier_id_value), 
                                        price_value, 
                                        int(units_stock_value), 
                                        description_value,
                                        category_value,
                                        category_description_value,
                                        company_name_value,
                                        company_phone_value)
        Product.Check_ID_Product() 
        self.window_1.destroy()
    
    def create_window_product_out(self): 
        self.window_1= tk.Toplevel(self.root)
        self.window_1.geometry(f"{int(self.screen_width*0.5)}x{int(self.screen_height*0.6)}")
        self.window_1.title('Phieu nhap hang')
        self.canvas_in = tk.Canvas(self.window_1, width=int(self.screen_width*0.5), height= int(self.screen_height*0.6), borderwidth= 0, highlightthickness= 0, background= 'white') 
        
        self.frame_search = tk.Frame(self.canvas_in, background='white', width= int(self.screen_width*0.5))
        self.frame_employee_form = tk.Frame(self.canvas_in, background='white')
        self.frame_employee_entry = tk.Frame(self.canvas_in, background='white')
        self.frame_product_form = tk.Frame(self.canvas_in, background='white')
        self.frame_product_entry = tk.Frame(self.canvas_in, background='white')
        self.frame_units_form = tk.Frame(self.canvas_in, background='white') 
        self.frame_units_entry = tk.Frame(self.canvas_in, background='white')
        self.frame_submit = tk.Frame(self.canvas_in, background='white')
        
        tk.Button(self.frame_search, text= 'Tim kiem:  ', font=('Arial', 15) , background='white', command= self.get_product_information).pack(side= tk.LEFT)
        tk.Entry(self.frame_search, textvariable= self.ID, font=('Arial', 15), width= 50, background='white').pack(side= tk.RIGHT)
        
        tk.Label(self.frame_employee_form, text= 'Thong tin khach hang', font=('Arial',15), background='white').pack()
        tk.Button(self.frame_employee_entry, text= 'Tim kiem', font=('Arial',15), background='white', command= self.get_customer_information).pack(pady=5)
        tk.Label(self.frame_employee_form, text='ID: ', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_employee_entry, textvariable=self.customerID, font=('Arial', 15), background='white').pack(pady= 5)
        # tk.Label(self.frame_employee_form, text='Name: ', font = ('Arial', 15), background='white').pack(pady=5)
        # tk.Entry(self.frame_employee_entry, textvariable=self.name, font=('Arial', 15), background='white').pack(pady= 5)
        # tk.Label(self.frame_employee_form, text='Address ', font = ('Arial', 15), background='white').pack(pady=5)
        # tk.Entry(self.frame_employee_entry, textvariable=self.price, font=('Arial', 15), background='white').pack(pady= 5)
        # tk.Label(self.frame_employee_form, text='Description: ', font = ('Arial', 15), background='white').pack(pady=5)
        # tk.Entry(self.frame_employee_entry, textvariable=self.description, font=('Arial', 15), background='white').pack(pady= 5)
        
        
        tk.Label(self.frame_product_form, text= 'Thong tin san pham', font=('Arial',15), background='white').pack()
        tk.Label(self.frame_product_form, text='ID: ', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_product_entry, textvariable=self.ID, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_product_form, text='Name: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_product_entry, textvariable=self.name, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_product_form, text='Price: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_product_entry, textvariable=self.price, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_product_form, text='Description: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_product_entry, textvariable=self.description, font=('Arial', 15), background='white').pack(pady= 5)
        
        
        tk.Label(self.frame_units_form, text= 'Thong tin so luong ', font=('Arial',15), background='white').pack(pady=5)
        tk.Label(self.frame_units_form, text='Units in stock:', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_units_entry, textvariable=self.unitsinstock, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_units_form, text='Units request: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_units_entry, textvariable=self.unitssupply, font=('Arial', 15), background='white').pack(pady= 5)
        
        tk.Button(self.frame_submit, text= 'Xuat kho', font = ('Arial', 15), background='white', command=self.update_information).pack(pady=5)
        
        self.canvas_in.pack()
        self.canvas_in.create_window(int(self.screen_width *0.25), int(self.screen_height*0.02), window= self.frame_search, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.08), int(self.screen_height*0.1), window= self.frame_employee_form, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.18), int(self.screen_height*0.13), window= self.frame_employee_entry, anchor= tk.N)
        
        self.canvas_in.create_line(int(self.screen_width*0.03), int(self.screen_height*0.28), int(self.screen_width*0.45), int(self.screen_height*0.28))
        
        self.canvas_in.create_window(int(self.screen_width *0.05), int(self.screen_height*0.3), window= self.frame_product_form, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.15), int(self.screen_height*0.33), window= self.frame_product_entry, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.3), int(self.screen_height*0.3), window= self.frame_units_form, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.4), int(self.screen_height*0.34), window= self.frame_units_entry, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.35), int(self.screen_height*0.45), window= self.frame_submit, anchor= tk.N)
        
        
    def get_customer_information(self): 
        ID_value = int(self.customerID.get())
        product_information = class_customer.Find_Customer(ID_value)
        print(product_information)
        
        # if product_information != None :
        #     self.name.set(f'{product_information[1]}')
        #     self.categoryid.set(f'{product_information[2]}')
        #     self.supplyid.set(f'{product_information[3]}')
        #     self.price.set(f'{product_information[4]}')
        #     self.unitsinstock.set(f'{product_information[5]}')
        #     self.description.set(f'{product_information[6]}')
        #     self.get_category_information()
        #     self.get_supplier_information()
        
        
        
        
# if __name__ == "__main__":
#     Product_In_Out(tk.Tk())
    