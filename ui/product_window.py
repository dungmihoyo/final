import tkinter as tk
import sys 
sys.path.append('./class/product')
import class_product as class_product
import class_supplier as class_supplier
import class_category as class_category

class Window_Product:  
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
        self.search_value_1 = tk.StringVar()
        
        self.flag_done_1 = False
        self.flag_done_2 = False
        self.flag_done_3 = False
        
        self.id_product = class_product.Get_ID()
        self.id_category = class_category.Get_ID()
        self.id_supplier = class_supplier.Get_ID()
    
        

    def Window_Add_Product(self): 
        

        self.ID.set(f'{self.id_product}')
        self.categoryid.set(f'{self.id_category}')
        self.supplyid.set(f'{self.id_supplier}')
        
        self.window_1= tk.Toplevel(self.root)
        self.window_1.geometry(f"{int(self.screen_width*0.5)}x{int(self.screen_height*0.6)}")
        self.window_1.title('Phieu nhap hang')
        self.canvas_in = tk.Canvas(self.window_1, width=int(self.screen_width*0.5), height= int(self.screen_height*0.6), borderwidth= 0, highlightthickness= 0, background= 'white') 
        self.flag_done_1 = False 
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
        tk.Label(self.frame_units_form, text='Units supply: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_units_entry, textvariable=self.unitssupply, font=('Arial', 15), background='white').pack(pady= 5)
        
        tk.Button(self.frame_submit, text= 'Add', font = ('Arial', 15), background='white', command= self.Add_Product).pack(pady=5)
        tk.Button(self.frame_submit, text= 'Exit', font = ('Arial', 15), background='white', command= self.window_1.destroy ).pack(pady=5)
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
        
    def Add_Product(self) : 
        
        self.flag_done_1 = True 
        name = self.name.get()
        price = float(self.price.get())
        unitinstock = (self.unitssupply.get())
        description = self.description.get()
        
        category_name = self.category.get()
        category_description = self.category_description.get()
        
        company_name = self.company_name.get() 
        company_phone = self.company_phone.get()
        
        product = class_product.Product(self.id_product, 
                                        name, 
                                        self.id_category, 
                                        self.id_supplier, 
                                        price, 
                                        unitinstock, 
                                        description, 
                                        category_name, 
                                        category_description, 
                                        company_name, 
                                        company_phone)
        product.Add_New_Product()
        self.window_1.destroy()
    
    def Window_Delete_Product(self): 
        self.window_1 = tk.Toplevel(self.root)
        self.window_1.geometry(f"{int(self.screen_width*0.2)}x{int(self.screen_height*0.1)}")
        self.canvas_2 = tk.Canvas(self.window_1, background= 'white', width= int(self.screen_width*0.2), height= int(self.screen_height*0.1))
        self.frame_delete = tk.Frame(self.window_1, background= 'white')
        self.flag_done_2 = False
        tk.Entry(self.frame_delete , textvariable= self.search_value_1, font= ('Arial', 15), background= 'white').pack(side= tk.LEFT,padx=5, pady= 5)
        tk.Button(self.frame_delete, text= 'Delete', font= ('Arial', 15), background= 'white', command= self.Delete_Product).pack(side= tk.RIGHT, padx=5, pady= 5)
        
        
        self.canvas_2.pack()
        self.canvas_2.create_window(int(self.screen_width*0.1), int(self.screen_height*0.03), window= self.frame_delete, anchor= tk.N)
    
    def Delete_Product(self):
        id = int(self.search_value_1.get())
        class_product.Delete_Product(id)
        self.flag_done_2 = True
        self.search_value_1.set('')
        self.window_1.destroy()
    
    def get_done_1 (self): 
        return self.flag_done_1 
    def get_done_2 (self): 
        return self.flag_done_2
    def get_done_3 (self): 
        return self.flag_done_3
        
# if __name__ == '__main__':
#     root = tk.Tk() 
#     Window_Product(root)
#     root.mainloop()