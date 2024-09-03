import tkinter as tk
from tksheet import Sheet 

import sys 
sys.path.append('./class/product')
import class_product as class_product

sys.path.append('./class/order')
import class_order_detail as class_order_detail
import class_shipping as class_shipping
import class_order as class_order 
import class_invoice as class_invoice

import datetime
class Order_Window: 
    def __init__(self, root, EmployeeID) :
        self.root = root
        # self.root.title('cua so chinh')
        
        self.screen_height = self.root.winfo_screenheight()
        self.screen_width = self.root.winfo_screenwidth()
        # self.root.geometry(f"{int(self.screen_width*0.5)}x{int(self.screen_height*0.6)}")
        
        # tk.Button(self.root, text="Nhap hang", command= self.Window_Order).pack(pady=20)
        
        self.ID_cus = tk.StringVar() 
        self.name_cus = tk.StringVar()
        self.phone = tk.StringVar()
        
        self.shippingid = tk.StringVar()
        self.shippingmethod = tk.StringVar()
        self.shippingcost = tk.StringVar() 
        self.shippingaddress = tk.StringVar()
        
        self.ProductID = tk.StringVar()
        self.ProductName = tk.StringVar() 
        self.ProductPrice = tk.StringVar() 
        self.Quantity = tk.StringVar() 
        self.TotalPrice = tk.StringVar() 
        
        self.ID = tk.StringVar()
        self.name = tk.StringVar()
        self.price = tk.StringVar()
        self.Order_ID = tk.StringVar()
        self.unitsinstock = tk.StringVar()
        
        self.orderdetail_id = tk.StringVar()
        self.ID_oder_details = class_order_detail.Get_ID()
        self.totalprice = tk.StringVar() 
        self.unitssupply = tk.StringVar()
        
        self.EmployeeID = EmployeeID
        self.InvoiceMethod = tk.StringVar()       
        self.totalall = tk.StringVar()
        self.totalall.set('0')
        self.data = self.set_data()
        self.count = 0 
        # self.root.mainloop()
    
    def Window_Order(self) : 
        shipping_id = class_shipping.Get_ID()
        self.shippingid.set(f'{shipping_id}')
        self.window_1= tk.Toplevel(self.root)
        self.window_1.geometry(f"{int(self.screen_width*0.5)}x{int(self.screen_height*0.8)}")
        self.window_1.title('Phieu nhan don')
        self.canvas_in = tk.Canvas(self.window_1, width=int(self.screen_width*0.5), height= int(self.screen_height*0.8), borderwidth= 0, highlightthickness= 0, background= 'white') 
        self.unit = 0 
        
        self.order_id = class_order.Get_ID()
        self.Order_ID.set(f'{self.order_id}')
        self.frame_id_order = tk.Frame(self.canvas_in, background='white')
        
        self.frame_customer_form = tk.Frame(self.canvas_in, background='white')
        self.frame_customer_entry = tk.Frame(self.canvas_in, background='white')
        
        self.frame_shipping_form = tk.Frame(self.canvas_in, background='white') 
        self.frame_shipping_entry = tk.Frame(self.canvas_in, background='white')
        self.frame_shipping_address = tk.Frame(self.canvas_in, background='white')
        
        self.frame_button = tk.Frame(self.canvas_in, background='white')
        self.frame_sheet = tk.Frame(self.canvas_in, background='white')
        
        self.frame_invoice_method = tk.Frame(self.canvas_in, background='white')
        self.frame_total_all = tk.Frame(self.canvas_in, background='white')
        self.frame_submit = tk.Frame(self.canvas_in, background='white')

        
        tk.Label(self.frame_id_order, text= 'Ma Order:', font=('Arial',15), background='white').pack(side=tk.LEFT)
        tk.Label(self.frame_id_order, text= f'{self.order_id}', font=('Arial',15), background='white').pack(side=tk.RIGHT)
        
        tk.Label(self.frame_customer_form, text= 'Thong tin khach hang', font=('Arial',15), background='white').pack()
        tk.Label(self.frame_customer_form, text='ID: ', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_customer_entry, textvariable=self.ID_cus, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_customer_form, text='Name: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_customer_entry, textvariable=self.name_cus, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_customer_form, text='Phone: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_customer_entry, textvariable=self.phone, font=('Arial', 15), background='white').pack(pady= 5)        
        tk.Label(self.frame_shipping_form, text= 'Thong tin van chuyen', font=('Arial',15), background='white').pack(pady=5)
        
        tk.Label(self.frame_shipping_form, text='Shipping_ID: ', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_shipping_entry, textvariable=self.shippingid, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_shipping_form, text='Shipping_Method: ', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_shipping_entry, textvariable=self.shippingmethod, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_shipping_form, text='Shipping_Cost: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_shipping_entry, textvariable=self.shippingcost, font=('Arial', 15), background='white').pack(pady= 5)
        
        tk.Label(self.frame_shipping_address, text='Address: ', font = ('Arial', 15), background='white').pack(pady=5, side=tk.LEFT)
        tk.Entry(self.frame_shipping_address, textvariable=self.shippingaddress, font=('Arial', 15), background='white', width= 60).pack(pady= 5, side= tk.RIGHT)
        
        
        tk.Button(self.frame_button, text= 'Them order', font=('Arial', 15) , background='white', command= self.window_add_order).pack(side= tk.LEFT, padx= 5)
        tk.Button(self.frame_button, text= 'Xoa order', font=('Arial', 15) , background='white', command= self.window_delete_order).pack(side= tk.LEFT, padx= 5)
        
        tk.Label(self.frame_invoice_method, text='Hinh thuc thanh toan', font = ('Arial', 15), background='white').pack(pady=5, side=tk.LEFT)
        tk.Entry(self.frame_invoice_method, textvariable=self.InvoiceMethod , font=('Arial', 15), background='white', width= 50).pack(pady= 5, side= tk.RIGHT)
         
        tk.Label(self.frame_total_all, text='Tong so tien', font = ('Arial', 15), background='white').pack(pady=5, side=tk.LEFT)
        tk.Entry(self.frame_total_all, textvariable=self.totalall, font=('Arial', 15), background='white', borderwidth= 0, highlightthickness= 0 ).pack(pady= 5, side= tk.RIGHT)
        
        tk.Button(self.frame_submit, text= 'Submit', font=('Arial', 15) , background='white', command= self.Add_Order).pack( padx= 5)
        
        self.Create_Sheet()
        
        self.canvas_in.pack()
        
        self.canvas_in.create_window(int(self.screen_width *0.06), int(self.screen_height*0.05), window= self.frame_id_order, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.08), int(self.screen_height*0.1), window= self.frame_customer_form, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.18), int(self.screen_height*0.13), window= self.frame_customer_entry, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.3), int(self.screen_height*0.1), window= self.frame_shipping_form, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.4), int(self.screen_height*0.14), window= self.frame_shipping_entry, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.25), int(self.screen_height*0.25), window= self.frame_shipping_address, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.4), int(self.screen_height*0.3), window= self.frame_button, anchor= tk.N)
        
        self.canvas_in.create_window(int(self.screen_width *0.25), int(self.screen_height*0.65), window= self.frame_invoice_method, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.15), int(self.screen_height*0.68), window= self.frame_total_all, anchor= tk.N)
        self.canvas_in.create_window(int(self.screen_width *0.45), int(self.screen_height*0.7), window= self.frame_submit, anchor= tk.N)
        
        
        
    def window_product(self): 
        self.window_2= tk.Toplevel(self.root)
        self.window_2.geometry(f"{int(self.screen_width*0.3)}x{int(self.screen_height*0.6)}")
        self.window_2.title('Phieu nhan don')
        self.canvas_2 = tk.Canvas(self.window_2, width=int(self.screen_width*0.3), height= int(self.screen_height*0.6), borderwidth= 0, highlightthickness= 0, background= 'white') 
        
        self.frame_search = tk.Frame(self.canvas_2, background='white')
        self.frame_product_form = tk.Frame(self.canvas_2, background='white')
        self.frame_product_entry = tk.Frame(self.canvas_2, background='white')
        
        self.frame_units_form = tk.Frame(self.canvas_2, background='white') 
        self.frame_units_entry = tk.Frame(self.canvas_2, background='white')
        
        self.frame_submit = tk.Frame(self.canvas_2, background='white')
        
        tk.Button(self.frame_search, text= 'Tim kiem:  ', font=('Arial', 15) , background='white', command= self.Find_Product).pack(side= tk.LEFT)
        tk.Entry(self.frame_search, textvariable= self.ID, font=('Arial', 15), width= 30, background='white').pack(side= tk.RIGHT)
        
        
        tk.Label(self.frame_product_form, text= 'Thong tin san pham', font=('Arial',15), background='white').pack()
        tk.Label(self.frame_product_form, text='ID: ', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_product_entry, textvariable=self.ID, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_product_form, text='Name: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_product_entry, textvariable=self.name, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_product_form, text='Price: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_product_entry, textvariable=self.price, font=('Arial', 15), background='white').pack(pady= 5)
        
        tk.Label(self.frame_units_form, text= 'Thong tin so luong ', font=('Arial',15), background='white').pack(pady=5)
        tk.Label(self.frame_units_form, text='Units in stock:', font = ('Arial', 15), background='white').pack(pady= 5)
        tk.Entry(self.frame_units_entry, textvariable=self.unitsinstock, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_units_form, text='Units order: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_units_entry, textvariable=self.unitssupply, font=('Arial', 15), background='white').pack(pady= 5)
        tk.Label(self.frame_units_form, text='Total Price: ', font = ('Arial', 15), background='white').pack(pady=5)
        tk.Entry(self.frame_units_entry, textvariable=self.totalprice, font=('Arial', 15), background='white').pack(pady= 5)
        
        tk.Button(self.frame_submit, text= 'Nhap don', font=('Arial', 15) , background='white', command= self.Submit).pack(side= tk.LEFT)
        
        
        self.canvas_2.pack()
        self.canvas_2.create_window(int(self.screen_width *0.15), int(self.screen_height*0.02), window= self.frame_search, anchor= tk.N)
        self.canvas_2.create_window(int(self.screen_width *0.08), int(self.screen_height*0.1), window= self.frame_product_form, anchor= tk.N)
        self.canvas_2.create_window(int(self.screen_width *0.18), int(self.screen_height*0.13), window= self.frame_product_entry, anchor= tk.N)
        self.canvas_2.create_line(int(self.screen_width*0.03), int(self.screen_height*0.28), int(self.screen_width*0.25), int(self.screen_height*0.28))
        self.canvas_2.create_window(int(self.screen_width *0.08), int(self.screen_height*0.3), window= self.frame_units_form, anchor= tk.N)
        self.canvas_2.create_window(int(self.screen_width *0.18), int(self.screen_height*0.34), window= self.frame_units_entry, anchor= tk.N)
        self.canvas_2.create_window(int(self.screen_width *0.2), int(self.screen_height*0.5), window= self.frame_submit, anchor= tk.N)
    
    
    
    
    
    
    def window_add_order(self) : 
        self.window_product( )
    
    def window_delete_order(self): 
        self.Delete_Order()
    
    def Find_Product(self) : 
        self.ID_value = int(self.ID.get())
        product_information = class_product.Find_Product(self.ID_value)
        product_information = list(product_information[0])
        print (product_information)
        if product_information != None :
            self.name.set(f'{product_information[1]}')
            self.price.set(f'{product_information[4]}')
            self.unitsinstock.set(f'{product_information[5]}')
            self.unitssupply.set('0')
            self.totalprice.set('0')
        
 
    def Submit(self): 
        quantity = int(self.unitssupply.get())
        price = int(self.price.get())
        total_price = float(quantity * price)
        sum = total_price + float(self.totalall.get())
        self.totalall.set(f'{sum}')
        self.totalprice.set(f'{total_price}')
        self.data.insert(self.count, [f'{self.ID_oder_details}', f'{self.name.get()}', f'{self.ID.get()}', f'{quantity}', f'{self.unitsinstock.get()}', f'{price}', f'{total_price}'])
        self.count += 1 
        self.ID_oder_details += 1 
        self.ID.set('')
        self.name.set('')
        self.price.set('')
        self.unitsinstock.set('')
        self.unitssupply.set('')
        self.totalprice.set('') 
        self.Create_Sheet()
        self.window_2.after(3000, self.window_2.destroy)
        
    def Delete_Order(self): 
        

        self.window_3= tk.Toplevel(self.root)
        self.window_3.geometry(f"{int(self.screen_width*0.2)}x{int(self.screen_height*0.1)}")
        self.window_3.title('Xoa order')
        self.canvas_3 = tk.Canvas(self.window_3, width=int(self.screen_width*0.2), height= int(self.screen_height*0.1), borderwidth= 0, highlightthickness= 0, background= 'white') 
        
        self.frame_find = tk.Frame(self.canvas_3, background='white') 
        tk.Button(self.frame_find, text='Delete', font = ('Arial', 15), background='white', command= self.Delete_Data).pack(pady=5, side= tk.RIGHT)
        tk.Entry(self.frame_find, textvariable=self.orderdetail_id, font=('Arial', 15), background='white').pack(pady= 5, side = tk.LEFT)
        
        self.canvas_3.pack()
        self.canvas_3.create_window(int(self.screen_width *0.1), int(self.screen_height*0.02), window= self.frame_find, anchor= tk.N)

        
        
    def Create_Sheet(self) : 
        if self.frame_sheet: 
            self.frame_sheet.destroy()
        print(self.data)
        self.frame_sheet = self.frame_sheet = tk.Frame(self.canvas_in, background='white')
        self.sheet_product = Sheet(self.frame_sheet, data= self.data , width= int(self.screen_width*0.4), height= int(self.screen_height*0.3), column_width= 200)
        self.sheet_product.headers([ 'ID_Order_Detail', 'Product Name', 'Product ID', 'Yeu cau', 'Trong kho', 'Don gia', 'Thanh tien'])
        self.sheet_product.pack(fill=tk.BOTH, expand=True)
        self.canvas_in.create_window(int(self.screen_width *0.25), int(self.screen_height*0.35), window= self.frame_sheet, anchor=tk.N)
    
    def Delete_Data(self): 
        for i in range(len(self.data)): 
            if self.data[i][0] == self.orderdetail_id.get(): 
                self.data.pop(i)
                break
        self.Create_Sheet()
        self.window_3.destroy()
    
    def set_data(self):
        
        data = [ ]
        for _ in range (100): 
            data.append(["" for _ in range(7)])
        return data 
    
    
    def Add_Order (self): 
        shipping = class_shipping.Shipping(int(self.shippingid.get()), self.shippingmethod.get(), float(self.shippingcost.get()), self.shippingaddress.get())
        shipping.Add_Shipping()
        
        invoice_id = class_invoice.Get_ID()
        invoice_date = class_invoice.Get_Time()
        invoice_method = self.InvoiceMethod.get()
        total = float(self.shippingcost.get()) + float(self.totalall.get())
        invoice = class_invoice.Invoice(invoice_id, invoice_date, invoice_method, total)
        invoice.Add_Invoice()
        
        
        for i in self.data: 
            if i[0] == '': 
                break
            order_detail = class_order_detail.Order_Details(int(i[0]), int(i[2]), int(i[3]), float(i[6]), int(self.order_id))
            number_unit = int(i[4]) - int(i[3])
            class_product.Update_Product(int(self.ID.get()), number_unit)
            order_detail.Add_Order_detail()
        
        order = class_order.Order(int(self.order_id), int(self.ID_cus), int(self.EmployeeID), int(invoice_id), int(self.shippingid.get(), f'{datetime.datetime.now()}'))
        order.Add_Order()
    
    
    def Get_Data(self): 
        return self.data
        
# if __name__ == "__main__":
#     Order_Window(tk.Tk()