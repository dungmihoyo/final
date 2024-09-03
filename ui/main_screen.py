from tksheet import Sheet
import tkinter as tk
from PIL import Image, ImageTk 
from login_window import Login_Window
from sheet_customer import Sheet_Customer
from sheet_product import Sheet_Product
from io import BytesIO 


import pandas as pd 
import product_window as product_window
import order_window as order_window
import product_in as product_in
from window_customer import Window_Customer

login = Login_Window(tk.Tk(), 'text')
class Main: 
    def __init__(self, window, title) :
        
        df = pd.read_csv('./asesrt/t.csv')
        self.city_name_in_vn = df['Ten']
        img = Image.open('./asesrt/avatar.jpg').resize((300,300))
        self.avatar = ImageTk.PhotoImage(img)
        
        self.window = window 
        self.screen_height = self.window.winfo_screenheight()
        self.screen_width = self.window.winfo_screenwidth()
        
        

        self.flag = login.get_flag()
        self.id = login.get_ID()
        
        self.window.title(title) 
        self.window.geometry(f"{int(self.screen_width)}x{int(self.screen_height)}")
        
        self.search_value = tk.StringVar()       
        
        self.profile_employee = login.get_profile()
        if (self.flag != 1) :
            self.order_window = order_window.Order_Window(self.window, self.profile_employee[0])
        
        self.win_cus = Window_Customer(self.window)
        self.product_in = product_in.Product_In_Out(self.window)
        self.product_window = product_window.Window_Product(self.window)
        
        self.flag_employee = False
        self.flag_product = False
        self.flag_check_product = False
        self.flag_order = False
        self.flag_customer = False 
        self.flag_warehouse = False
        # self.flag_order = False 
        # self.flag_warehouse = False 
        
        self.canvas_task = tk.Canvas(self.window, width= int(self.screen_width*0.2), height= int(self.screen_height), borderwidth= 3, highlightthickness= 0 , background='black') 
        self.canvas_information = self.create_canvas()
        self.canvas_on = tk.Canvas(self.canvas_information, width= int(self.screen_width*0.8), height= int(self.screen_height*0.1), borderwidth= 3, highlightthickness= 0 , background='yellow') 
        
        self.frame_user = tk.Frame(self.canvas_task, borderwidth= 0, highlightthickness= 0, background= 'white')
        self.frame_product = tk.Frame(self.canvas_task, borderwidth= 0, highlightthickness= 0, background= 'yellow')
        self.frame_employee = tk.Frame(self.canvas_task, borderwidth= 0, highlightthickness= 0, background= 'yellow') 
        self.frame_product_manager = tk.Frame(self.canvas_task, borderwidth= 0, highlightthickness= 0, background= 'yellow') 
        self.frame_manager_op = tk.Frame(self.canvas_task, borderwidth= 0, highlightthickness= 0, background= 'yellow') 
        self.frame_order = tk.Frame(self.canvas_task, borderwidth= 0, highlightthickness= 0, background= 'yellow') 

        self.frame_customer = tk.Frame(self.canvas_task, borderwidth= 0, highlightthickness= 0, background= 'yellow') 
    
        
        self.frame_search = tk.Frame(self.canvas_information)
        self.frame_bar = tk.Frame(self.canvas_information) 
        self.frame_filter = tk.Frame(self.canvas_information)
        self.frame_sheet_0= tk.Frame(self.canvas_information)
        self.frame_sheet_1= tk.Frame(self.canvas_information)
        self.frame_sheet_2= tk.Frame(self.canvas_information)
        self.frame_sheet_3= tk.Frame(self.canvas_information)
        self.frame_sheet_4= tk.Frame(self.canvas_information)
        self.frame_sheet_5= tk.Frame(self.canvas_information)
       
        
        if(self.flag == 1) : 
            tk.Label(self.frame_user,  text = 'Admin', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.004),background='white').pack()
            tk.Button(self.frame_product, text='Danh muc san pham', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.window_information_product).pack()
            # tk.Button(self.frame_customer, text='Danh muc khach hang ', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.window_customer).pack()
            tk.Button(self.frame_product_manager, text='Kiem ke hang hoa', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.check_product).pack()            
            tk.Label(self.frame_manager_op, text= 'Quan li kho', font=('Arial', 15), borderwidth=0 , highlightthickness= 0).pack() 
            tk.Button(self.frame_manager_op, text='Vi tri hang hoa', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            tk.Button(self.frame_manager_op, text='Sap xep hang hoa', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
        if(self.flag == 2): 
            tk.Button(self.frame_user, text = 'Employee', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.004),background='white', command= self.create_information_employee).pack(pady= 5)
            tk.Button(self.frame_product, text='Danh muc san pham', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.window_information_product).pack()
            
            tk.Button(self.frame_customer, text='Danh muc khach hang ', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.window_customer).pack()
            
            
            tk.Label(self.frame_product_manager, text= 'Quan li san pham', font=('Arial', 15), borderwidth=0 , highlightthickness= 0).pack() 
            tk.Button(self.frame_product_manager, text='Kiem ke hang hoa', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.check_product).pack()
            
            tk.Label(self.frame_manager_op, text= 'Quan li kho', font=('Arial', 15), borderwidth=0 , highlightthickness= 0).pack() 
            tk.Button(self.frame_manager_op, text='Vi tri hang hoa', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            tk.Button(self.frame_manager_op, text='Sap xep hang hoa', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            
            tk.Label(self.frame_order, text= 'Don hang, van chuyen', font=('Arial', 15), borderwidth=0 , highlightthickness= 0).pack() 
            tk.Button(self.frame_order, text='Thong tin don hang', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.window_order).pack()
            
            
        if(self.flag == 3): 
            tk.Button(self.frame_user, text = 'Manger', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.004),background='white', command= self.create_information_employee).pack()
            tk.Button(self.frame_product, text='Danh muc san pham', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.window_information_product).pack()

            tk.Label(self.frame_product, text= 'Quan li san pham', font=('Arial', 15), borderwidth=0 , highlightthickness= 0).pack() 
            tk.Button(self.frame_product, text='Kiem ke hang hoa', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.check_product).pack()
            tk.Button(self.frame_product, text='Chinh sua danh sach', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            
            tk.Label(self.frame_manager_op, text= 'Quan li kho', font=('Arial', 15), borderwidth=0 , highlightthickness= 0).pack() 
            tk.Button(self.frame_manager_op, text='Vi tri hang hoa', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            tk.Button(self.frame_manager_op, text='Sap xep hang hoa', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            
            tk.Label(self.frame_order, text= 'Don hang, van chuyen', font=('Arial', 15), borderwidth=0 , highlightthickness= 0).pack() 
            tk.Button(self.frame_order, text='Thong tin don hang', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            tk.Button(self.frame_order, text='Chinh sua thong tin don hang', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            
            tk.Label(self.frame_employee, text= 'Quan li nhan vien', font=('Arial', 15), borderwidth=0 , highlightthickness= 0).pack() 
            tk.Button(self.frame_employee, text='Danh muc nhan vien', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            tk.Button(self.frame_employee, text='Chinh sua danh sach', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white').pack()
            
            
        self.canvas_task.pack(side= tk.LEFT) 
        
        self.canvas_task.create_window(self.screen_width*0.1, 0, window = self.frame_user, anchor= tk.N)
        # self.canvas_task.create_window(self.screen_width*0.1, self.screen_height*0.1, window = self.frame_product, anchor= tk.N)
        # self.canvas_task.create_window(self.screen_width*0.1, self.screen_height*0.15, window = self.frame_customer, anchor= tk.N)
        # self.canvas_task.create_window(self.screen_width*0.1, self.screen_height*0.25, window = self.frame_product_manager, anchor= tk.N)
        self.canvas_task.create_window(self.screen_width*0.1, self.screen_height*0.45, window= self.frame_manager_op, anchor= tk.N)
        # self.canvas_task.create_window(self.screen_width*0.1, self.screen_height*0.55, window= self.frame_order, anchor= tk.N)
        # self.canvas_task.create_window(self.screen_width*0.1, self.screen_height*0.6, window= self.frame_employee, anchor= tk.N)
        

        if self.flag != 0 :  
            self.window.mainloop()
    def clear_widget(self, frame): 
        for widget in frame.winfo_children():
            widget.destroy()     
    
    def clear_canvas(self): 
        for widget in self.canvas_information.winfo_children(): 
            widget.destroy()
            
    def create_canvas(self):
        canvas = tk.Canvas(self.window, width= int(self.screen_width*0.8), height= int(self.screen_height), borderwidth= 3, highlightthickness= 0 , background='blue') 
        canvas.pack(side= tk.RIGHT,  fill= tk.BOTH, expand=True)
        return canvas
    
    def delete_canvas (self): 
        if self.canvas_information: 
            self.canvas_information.destroy()
            self.canvas_information = None
    


    def create_information_employee(self): 
        
        self.delete_canvas()
        self.flag_customer = False 
        self.flag_warehouse = False 
        self.flag_product = False  
        self.flag_check_product = False
        self.flag_order = False 
        self.canvas_information = self.create_canvas()
        
        self.frame_bg_1 = tk.Frame(self.canvas_information, background = 'black', width= int(self.screen_width*0.5), height= int(self.screen_height*0.8))
        
        self.frame_employee_profile_img = tk.Frame(self.canvas_information, background= 'white')
        self.frame_employee_profile_personal = tk.Frame(self.canvas_information, background='white') 
        self.frame_label_personal = tk.Frame(self.frame_employee_profile_personal, background='white')
        self.frame_employee_name = tk.Frame(self.frame_employee_profile_personal, background='white')
        self.frame_employee_age = tk.Frame(self.frame_employee_profile_personal, background='white')
        self.frame_employee_sex = tk.Frame(self.frame_employee_profile_personal, background='white')
        self.frame_employee_bod = tk.Frame(self.frame_employee_profile_personal, background='white')

        
        
        self.frame_employee_profile_address = tk.Frame(self.canvas_information, background='white') 
        self.frame_employee_profile_work = tk.Frame(self.canvas_information, background='white') 
        self.frame_employee_profile_contact = tk.Frame(self.canvas_information, background='white') 
        
        
        self.frame_label_personal.pack()
        self.frame_employee_name.pack()
        self.frame_employee_age.pack()
        self.frame_employee_sex.pack()
        self.frame_employee_bod.pack()
        
        tk.Label(self.frame_employee_profile_img, image= self.avatar).pack()
        tk.Label(self.frame_employee_profile_img, text= f'ID: {self.profile_employee[0]}', font= ('Arial', 20)).pack()
        
        tk.Label(self.frame_label_personal, text= f"Thong tin ca nhan", font= ('Arial', 20), anchor= tk.W).pack(pady= 10)
        tk.Label(self.frame_employee_name, text= f"Ho va ten: ", font= ('Arial', 15), anchor= tk.W).pack(side = tk.LEFT, pady= 5)
        tk.Label(self.frame_employee_age, text= f"Tuoi: ", font= ('Arial', 15), anchor= tk.W).pack(side= tk.LEFT, pady= 5)
        tk.Label(self.frame_employee_sex, text= f"Gioi Tinh: ", font= ('Arial', 15), anchor= tk.W).pack(side= tk.LEFT, pady= 5)
        tk.Label(self.frame_employee_bod, text= f"Ngay sinh: ", font= ('Arial', 15), anchor= tk.W).pack(side= tk.LEFT, pady= 5)
        
        tk.Label(self.frame_employee_name, text = f'{self.profile_employee[1]}', font = ('Arial', 15)).pack(side= tk.RIGHT, padx= 32, pady= 5)
        tk.Label(self.frame_employee_age, text = f'{self.profile_employee[2]}', font = ('Arial', 15)).pack(side= tk.RIGHT, padx= 107, pady= 5)
        tk.Label(self.frame_employee_sex, text = f'{self.profile_employee[3]}', font = ('Arial', 15)).pack(side= tk.RIGHT, padx=52, pady= 5)
        tk.Label(self.frame_employee_bod, text = f'{self.profile_employee[4]}', font = ('Arial', 15)).pack(side= tk.RIGHT, pady= 5)
        
        

        
        tk.Label(self.frame_employee_profile_address, text= f"Dia chi", font= ('Arial', 20), anchor= tk.W,).pack(pady= 5)
        tk.Label(self.frame_employee_profile_address, text= f"Tinh/Thanh pho:      {self.profile_employee[9]}", font= ('Arial', 15), anchor= tk.W).pack(pady= 5)
        tk.Label(self.frame_employee_profile_address, text= f"Quan/Huyen:          {self.profile_employee[10]}", font= ('Arial', 15), anchor= tk.W).pack(pady= 5)
        tk.Label(self.frame_employee_profile_address, text= f"Xa/Phuong/Thi tran:  {self.profile_employee[11]}", font= ('Arial', 15), anchor= tk.W).pack(pady= 5)
        tk.Label(self.frame_employee_profile_address, text= f"Mo ta chi tiet:      {self.profile_employee[12]}", font= ('Arial', 15), anchor= tk.W).pack(pady= 5)
        
        tk.Label(self.frame_employee_profile_work, text= f"Cong viec/ Khu vuc", font= ('Arial', 20), anchor= tk.W).pack(pady= 5)
        tk.Label(self.frame_employee_profile_work, text= f"Vi tri:        {self.profile_employee[8]}", font= ('Arial', 15), anchor= tk.W).pack(pady= 5)
        tk.Label(self.frame_employee_profile_work, text= f"Khu vuc:           Kho hang", font= ('Arial', 15), anchor= tk.W).pack(pady= 5)
        tk.Label(self.frame_employee_profile_work, text= f"Ngay lam viec: {self.profile_employee[5]}", font= ('Arial', 15), anchor= tk.W).pack(pady= 5)
        
        tk.Label(self.frame_employee_profile_contact, text= f"Thong tin lien lac", font= ('Arial', 20), anchor= tk.W).pack(pady= 5)
        tk.Label(self.frame_employee_profile_contact, text= f"So dien thoai:       {self.profile_employee[6]}", font= ('Arial', 15), anchor= tk.W).pack(pady= 5)
        tk.Label(self.frame_employee_profile_contact, text= f"Email:         {self.profile_employee[7]}", font= ('Arial', 15), anchor= tk.W).pack(pady= 5)
        
        if self.flag_employee == False : 
            
            self.canvas_information.create_window(int(self.screen_width* 0.3), int(self.screen_height* 0.05), window= self.frame_bg_1, anchor= tk.N )
            self.canvas_information.create_window(int(self.screen_width* 0.2), int(self.screen_height* 0.1), window= self.frame_employee_profile_img, anchor= tk.N )
            self.canvas_information.create_window(int(self.screen_width* 0.2), int(self.screen_height* 0.45), window= self.frame_employee_profile_personal, anchor= tk.N )
            

            self.canvas_information.create_window(int(self.screen_width* 0.4), int(self.screen_height* 0.1), window= self.frame_employee_profile_address, anchor= tk.N )
            self.canvas_information.create_window(int(self.screen_width* 0.4), int(self.screen_height* 0.33), window= self.frame_employee_profile_work, anchor= tk.N )
            self.canvas_information.create_window(int(self.screen_width* 0.4), int(self.screen_height* 0.53), window= self.frame_employee_profile_contact, anchor= tk.N )
            self.flag_employee = True
                
                   
    def window_information_product(self):  
        
        self.delete_canvas()
        self.frame_key = None 
        print (self.canvas_information == None)
        self.canvas_information = self.create_canvas()
        
        self.flag_warehouse = False 
        self.flag_customer = False 
        self.flag_employee = False
        self.flag_check_product = False
        self.flag_order = False 
        
        self.frame_search = tk.Frame(self.canvas_information, background='white')
        self.frame_bar = tk.Frame(self.canvas_information, background= 'white') 
 
        self.frame_filter = tk.Frame(self.canvas_information, background= 'white')
        self.frame_sheet_0= tk.Frame(self.canvas_information, background= 'white')
        self.frame_sheet_1= tk.Frame(self.canvas_information, background= 'white')
        self.frame_sheet_2= tk.Frame(self.canvas_information, background= 'white')
        self.frame_sheet_3= tk.Frame(self.canvas_information, background= 'white')
        self.frame_sheet_4= tk.Frame(self.canvas_information, background= 'white')
        self.frame_sheet_5= tk.Frame(self.canvas_information, background= 'white')
        
        if self.flag_product == False : 
            
            tk.Entry(self.frame_search, font=('Arial', 15), textvariable= self.search_value, borderwidth= 0, highlightthickness= 0, width= 100, background= 'white').pack(side= tk.RIGHT)
            tk.Button(self.frame_search, text ='Tim kiem', font = ('Arial', 15), borderwidth= 0, highlightthickness= 0, command= self.window_0, background= 'white').pack(side= tk.LEFT)
             
            tk.Button(self.frame_filter, text = 'Bo loc', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, background= 'white').pack()
            
            tk.Button(self.frame_bar, text= 'Tat ca', font= ('Arial', 15), borderwidth= 0, highlightthickness=0, width= 20, command= self.window_1, background= 'white').pack(side=tk.LEFT, padx= 20)
            tk.Button(self.frame_bar, text= 'Hang ton kho ', font= ('Arial', 15), borderwidth= 0, highlightthickness=0, width= 20, command= self.window_2, background= 'white').pack(side=tk.LEFT, padx= 20)
            tk.Button(self.frame_bar, text= 'Hang sap het', font= ('Arial', 15), borderwidth= 0, highlightthickness=0, width= 20, background= 'white', command= self.window_3).pack(side=tk.LEFT, padx= 20)
            tk.Button(self.frame_bar, text= 'Hang het', font= ('Arial', 15), borderwidth= 0, highlightthickness=0, width= 20, background= 'white', command= self.window_4).pack(side=tk.LEFT, padx= 20)
            
            
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height *0.01), window= self.frame_search, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.05), int(self.screen_height *0.05), window= self.frame_filter, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height * 0.1), window= self.frame_bar, anchor= tk.N)
            
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_0, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_1, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_2, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_3, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_4, anchor= tk.N)
            self.flag_product = True
            
                      
    def window_0(self): 
        
        if self.frame_key: 
            # self.clear_widget(self.frame_key)  
            self.frame_key.destroy()
        self.frame_sheet_0= tk.Frame(self.canvas_information, background= 'white')
        search_value = self.search_value.get()       
        sheet = Sheet_Product(self.frame_sheet_0)
        sheet.sheet_search_product(int(search_value))
        self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_0, anchor= tk.N)
        self.frame_key= self.frame_sheet_0
        
    def window_1(self): 
        
        if self.frame_key: 
            # self.clear_widget(self.frame_key)  
            self.frame_key.destroy()
            
        self.frame_sheet_1 = tk.Frame(self.canvas_information, background= 'white')
        sheet = Sheet_Product(self.frame_sheet_1)
        sheet.sheet_product()
        self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_1, anchor= tk.N)
        
        self.frame_key = self.frame_sheet_1
        
    def window_2 (self):  
        
        if self.frame_key: 
            # self.clear_widget(self.frame_key)  
            self.frame_key.destroy()
            
        self.frame_sheet_2= tk.Frame(self.canvas_information, background= 'white')
        self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_2, anchor= tk.N)
        sheet = Sheet_Product(self.frame_sheet_2)
        sheet.sheet_product_units()
        
        self.frame_key = self.frame_sheet_2
        
    def window_3 (self):
        if self.frame_key: 
            # self.clear_widget(self.frame_key) 
            self.frame_key.destroy()
            
        self.frame_sheet_3= tk.Frame(self.canvas_information, background= 'white')
        sheet = Sheet_Product(self.frame_sheet_3)
        sheet.sheet_product_units()
        self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_3, anchor= tk.N)
        
        self.frame_key = self.frame_sheet_3
    def window_4 (self):
        if self.frame_key: 
            # self.clear_widget(self.frame_key) 
            self.frame_key.destroy()
            
        self.frame_sheet_4= tk.Frame(self.canvas_information, background= 'white')
        sheet = Sheet_Product(self.frame_sheet_4)
        sheet.sheet_product_units_zero() 
        self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.18), window= self.frame_sheet_4, anchor= tk.N)
        self.frame_key = self.frame_sheet_4




    def check_product(self): 
        
        self.delete_canvas()
        self.flag_customer = False
        self.flag_warehouse = False
        self.flag_product = False  
        self.flag_employee = False
        self.flag_order = False 
        self.canvas_information = self.create_canvas()          
        
        self.frame_key_1 = None
        self.frame_check_0 = tk.Frame(self.canvas_information, background= 'white')
        self.frame_check_1 = tk.Frame(self.canvas_information, background= 'white')
        self.frame_check_2 = tk.Frame(self.canvas_information)
        self.frame_check_3 = tk.Frame(self.canvas_information)       
        self.frame_check_4 = tk.Frame(self.canvas_information, background= 'white')
        self.frame_check_5 = tk.Frame(self.canvas_information)
        self.frame_check_6 = tk.Frame(self.canvas_information)     
                  
        tk.Entry(self.frame_check_0, font=('Arial', 15), textvariable= self.search_value, highlightthickness= 0, width= 120).pack(side= tk.RIGHT)
        tk.Button(self.frame_check_0, text ='Add', font = ('Arial', 15), borderwidth= 0, highlightthickness= 0, command= self.window_7, background= 'white').pack(side= tk.LEFT)     
        tk.Button(self.frame_check_0, text ='Change', font = ('Arial', 15), borderwidth= 0, highlightthickness= 0, background='white').pack(side= tk.LEFT)     
        tk.Button(self.frame_check_0, text ='Delete', font = ('Arial', 15), borderwidth= 0, highlightthickness= 0, command= self.window_9, background='white').pack(side= tk.LEFT)     
        tk.Button(self.frame_check_0, text ='Search', font = ('Arial', 15), borderwidth= 0, highlightthickness= 0, command= self.window_5, background='white').pack(side= tk.LEFT)   
        
        tk.Button(self.frame_check_1, text= 'Nhap hang', font=('Arial', 15), borderwidth= 0, command= self.product_in.create_window_product_in, background='white').pack(side= tk.LEFT, padx= 5)                                          
        tk.Button(self.frame_check_1, text= 'Xuat Hang', font=('Arial', 15), borderwidth= 0, background= 'white').pack(side= tk.LEFT, padx= 5)   
        tk.Button(self.frame_check_1, text= 'Kiem hang', font=('Arial', 15), borderwidth= 0, background= 'white').pack(side= tk.LEFT, padx= 5)   
        
        sheet = Sheet_Product(self.frame_check_4)
        sheet.sheet_product()                                 
        self.frame_key_1 = self.frame_check_4                        
                                                                      
        if self.flag_check_product == False:
            
            self.canvas_information.create_window(int(self.screen_width*0.42), int(self.screen_height*0.00), window= self.frame_check_0, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.096), int(self.screen_height*0.03), window= self.frame_check_1, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.1), window= self.frame_check_2, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.6), int(self.screen_height*0.1), window= self.frame_check_3, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.08), window= self.frame_check_4, anchor= tk.N)
            self.flag_check_product = True
    
    
    def window_5 (self) : 
        if self.frame_key_1: 
            self.frame_key_1.destroy()
        search_value = self.search_value.get()    
        self.frame_check_2 = tk.Frame(self.canvas_information, background= 'white')
        self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.08), window= self.frame_check_2, anchor= tk.N)
        sheet = Sheet_Product(self.frame_check_2)
        sheet.sheet_search_product(int(search_value))
        self.frame_key_1 = self.frame_check_2
        
    def window_6 (self): 
        if self.frame_key_1: 
            self.frame_key_1.destroy()
        self.frame_check_4 = tk.Frame(self.canvas_information, background= 'white')
        self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.08), window= self.frame_check_4, anchor= tk.N)
        sheet = Sheet_Product(self.frame_check_4)
        sheet.sheet_product()
        self.frame_key_1 = self.frame_check_4
    
    def window_7 (self):
        self.product_window.Window_Add_Product() 
        if self.product_window.get_done_1() : 
            self.window_6()
    
    def window_9 (self) : 
        self.product_window.Window_Delete_Product() 
        if self.product_window.get_done_2() : 
            self.window_6()
        
        
    def window_order(self) : 
        self.delete_canvas()
        self.flag_product = False 
        self.flag_check_product = False
        self.flag_employee = False 
        self.canvas_information = self.create_canvas()
        self.search_order = tk.StringVar()
        self.frame_search_order = tk.Frame(self.canvas_information, background= 'white')
        self.frame_button_order = tk.Frame(self.canvas_information, background= 'white')
        self.frame_order = tk.Frame(self.canvas_information, background= 'white')
        
        tk.Button(self.frame_search_order, text='Tim kiem', font=('Arial',15), background='white').pack(side=tk.LEFT, padx= 5) 
        tk.Entry(self.frame_search_order, textvariable=self.search_order, font=('Arial',15), background='white', width= 100).pack(side=tk.RIGHT, padx= 5)      
        
        tk.Button(self.frame_button_order, text='Don hang moi', font=('Arial',15), background='white', command= self.order_window.Window_Order).pack(side=tk.LEFT, padx= 5) 
        tk.Button(self.frame_button_order, text='Xoa don hang', font=('Arial',15), background='white').pack(side=tk.LEFT, padx= 5) 
    
    
        self.canvas_information.pack()
        self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.05), window= self.frame_search_order, anchor= tk.N)
        self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.1), window= self.frame_button_order, anchor= tk.N)
    
    def window_customer(self): 
        self.delete_canvas()
        self.canvas_information = self.create_canvas()
        
        self.flag_warehouse = False 
        self.flag_order = False
        self.flag_product = False 
        self.flag_check_product = False
        self.flag_employee = False 

        self.search_customer = tk.StringVar()
        self.frame_key_2 = None
        self.frame_search_customer = tk.Frame(self.canvas_information, background= 'white')
        
        self.frame_button_customer = tk.Frame(self.canvas_information, background= 'white')
        
        self.frame_sheet_customer_0 = tk.Frame(self.canvas_information, background= 'white')
        self.frame_sheet_customer_1 = tk.Frame(self.canvas_information, background= 'white')
        self.frame_sheet_customer_2 = tk.Frame(self.canvas_information, background= 'white')
        self.frame_sheet_customer_3 = tk.Frame(self.canvas_information, background= 'white')
        
        self.frame_filter_customer = self.create_scrollable_buttons(self.canvas_information)
        
        
        tk.Button(self.frame_search_customer, text= 'Tim kiem', font= ('Arial', 15), background= 'white', borderwidth= 0, command= self.sheet_customer_1).pack(side= tk.LEFT, padx= 5)
        tk.Entry(self.frame_search_customer, textvariable=self.search_customer, font= ('Arial', 15), background= 'white', width= int(self.screen_width*0.06), borderwidth= 0 ).pack(side= tk.RIGHT, padx= 5)    
    
        tk.Button(self.frame_button_customer, text= 'Add', font= ('Arial', 15), background= 'white', width= 10, command= self.Add_Cus).pack(side= tk.TOP, padx= 5, pady= 5)
        tk.Button(self.frame_button_customer, text= 'Change', font= ('Arial', 15), background= 'white', width= 10, command= self.Change_Cus).pack(side= tk.TOP, padx= 5, pady= 5)
        tk.Button(self.frame_button_customer, text= 'Delete', font= ('Arial', 15), background= 'white', width= 10, command= self.Delete_Cus).pack(side= tk.TOP, padx= 5, pady= 5)
        
        sheet = Sheet_Customer(self.frame_sheet_customer_0)
        sheet.sheet_customer()
        self.frame_key_2 = self.frame_sheet_customer_0
        
        if self.flag_customer == False : 
            self.canvas_information.create_window(int(self.screen_width*0.4), int(self.screen_height*0.03), window= self.frame_search_customer, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.1), int(self.screen_height*0.08), window= self.frame_filter_customer, anchor= tk.N)
            self.canvas_information.create_window(int(self.screen_width*0.1), int(self.screen_height*0.6), window= self.frame_button_customer, anchor= tk.N)
            
            self.canvas_information.create_window(int(self.screen_width*0.48), int(self.screen_height*0.08), window= self.frame_sheet_customer_0, anchor= tk.N)

        
    def sheet_customer(self) : 
        if self.frame_key_2 : 
            self.frame_key_2.destroy() 
        self.frame_sheet_customer_0= tk.Frame(self.canvas_information, background= 'white')
        sheet = Sheet_Customer(self.frame_sheet_customer_0)
        sheet.sheet_customer() 
        self.canvas_information.create_window(int(self.screen_width*0.47), int(self.screen_height*0.08), window= self.frame_sheet_customer_0, anchor= tk.N)
        
    def sheet_customer_1(self) : 
        if self.frame_key_2 : 
            self.frame_key_2.destroy() 
        search_value = int(self.search_customer.get())
        self.frame_sheet_customer_1 = tk.Frame(self.canvas_information, background= 'white')
        sheet = Sheet_Customer(self.frame_sheet_customer_1)
        sheet.sheet_customer_search(search_value) 
        self.frame_key_2 = self.frame_sheet_customer_1
        self.canvas_information.create_window(int(self.screen_width*0.47), int(self.screen_height*0.08), window= self.frame_sheet_customer_1, anchor= tk.N)
    
    def sheet_customer_2 (self) : 
        
        if self.frame_key_2 : 
            self.frame_key_2.destroy() 
        search_value = int(self.search_customer.get())
        self.frame_sheet_customer_2 = tk.Frame(self.canvas_information, background= 'white')
        sheet = Sheet_Customer(self.frame_sheet_customer_2)
        sheet.sheet_customer_search(search_value) 
        self.frame_key_2 = self.frame_sheet_customer_2
        self.canvas_information.create_window(int(self.screen_width*0.47), int(self.screen_height*0.08), window= self.frame_sheet_customer_2, anchor= tk.N)
    
    def Add_Cus(self): 
        self.win_cus.Window_Add_Customer()
        if self.win_cus.get_done_1():
            self.sheet_customer()
    
    def Change_Cus(self): 
        self.win_cus.Window_Change_Customer()
        if self.win_cus.get_done_2():
            self.sheet_customer() 
    
    def Delete_Cus(self): 
        self.win_cus.Window_Delete_Customer()
        if self.win_cus.get_done_3():
            self.sheet_customer()

    def on_frame_configure(self,event):
        self.canvas_information.configure(scrollregion=self.canvas_information.bbox("all"))
        
    def create_scrollable_buttons(self,canvas ):
        # Tạo Frame chính để chứa Canvas và Scrollbar
        main_frame = tk.Frame(canvas, width=int(self.screen_width*0.04))
        main_frame.pack(fill='both', expand=True)

        # Tạo Canvas và Scrollbar
        canvas = tk.Canvas(main_frame, bg='white', height=int(self.screen_height*0.5), width=int(self.screen_width*0.1))
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)

        # Tạo một Frame để chứa các nút trong Canvas
        button_frame = tk.Frame(canvas, bg='white')

        # Tạo cửa sổ trong Canvas để chứa Frame
        canvas.create_window((0, 0), window=button_frame, anchor='nw')

        # Cập nhật vùng cuộn của Canvas khi kích thước của Frame thay đổi
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        button_frame.bind("<Configure>", on_frame_configure)

        # Đặt Canvas và Scrollbar vào Frame chính
        canvas.pack(side='right', fill='both', expand=True)
        scrollbar.pack(side='left', fill='y')
        canvas.configure(yscrollcommand=scrollbar.set)

        # Thêm nút vào Frame
        tk.Label(button_frame, text= 'Bo loc', font= ('Arial', 15), background= 'white', width= 10, borderwidth= 0).pack(side= tk.TOP, padx= 5)
        for i in self.city_name_in_vn: 
            tk.Button(button_frame, text= i, font= ('Arial', 10), background= 'white', width= 10, borderwidth= 0, command= self.sheet_customer_2).pack(side= tk.TOP)

        return main_frame
    
    def window_add_customer (self) : 
        self.window
    
    
    
if __name__ == "__main__":
    Main(tk.Tk(), "UI")