import tkinter as tk
import sys 
sys.path.append('./class/human')
import class_customer as class_customer


class Window_Customer: 
    def __init__(self, root) :
        self.root = root 
        self.screen_height = self.root.winfo_screenheight()
        self.screen_width = self.root.winfo_screenwidth()
        
        self.ID = tk.StringVar()
        self.name = tk.StringVar()
        self.phone = tk.StringVar() 
        
        self.city = tk.StringVar()
        self.area = tk.StringVar()
        self.commune = tk.StringVar() 
        self.description = tk.StringVar()
        id =  class_customer.Get_ID()
        self.ID.set(f'{id}')
        self.ID_search = tk.StringVar()
        
        self.search_value_1 = tk.StringVar()
        self.search_value_2 = tk.StringVar()
        self.flag_done_1 = False
        self.flag_done_2 = False
        self.flag_done_3 = False
        
    
    def Window_Add_Customer(self) : 
        self.window = tk.Toplevel(self.root)
        self.window.geometry(f"{int(self.screen_width*0.2)}x{int(self.screen_height*0.7)}")
        self.window.title("Cua so them nguoi dung moi")
        self.flag_dome_1 = False
        self.canvas_1 = tk.Canvas(self.window, width= int(self.screen_width*0.2), height= int(self.screen_height*0.7), background= 'white')
        
        self.frame_cus_label = tk.Frame(self.canvas_1, background= 'white')
        self.frame_cus_infor = tk.Frame(self.canvas_1, background= 'white')
        self.frame_cus_add = tk.Frame(self.canvas_1, background= 'white')
        self.frame_cus_submit  = tk.Frame(self.canvas_1, background= 'white')
        
        tk.Label(self.frame_cus_label, text= 'Thong tin khach hang moi', font= ('Arial', 15), background= 'white', borderwidth= 0).pack()
        
        tk.Label(self.frame_cus_infor, text= 'Ma khach hang', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5 )
        tk.Entry(self.frame_cus_infor, textvariable= self.ID, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_cus_infor, text= 'Ten khach hang', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_cus_infor, textvariable= self.name, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_cus_infor, text= 'So dien thoai', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_cus_infor, textvariable= self.phone, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        

        tk.Label(self.frame_cus_add, text= 'Tinh/ThanhPho', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5 )
        tk.Entry(self.frame_cus_add, textvariable= self.city, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_cus_add, text= 'Quan/Huyen', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_cus_add, textvariable= self.area, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_cus_add, text= 'Xa/Phuong/ThiTran', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_cus_add, textvariable= self.commune, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_cus_add, text= 'Mo ta them', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_cus_add, textvariable= self.description, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        
        tk.Button(self.frame_cus_submit, text= 'Add', font= ('Arial', 15), background= 'white', command= self.Add_Customer).pack(side= tk.LEFT, padx=5, pady= 5)
        tk.Button(self.frame_cus_submit, text= 'Exit', font= ('Arial', 15), background= 'white', command= self.window .destroy).pack(side= tk.RIGHT, padx=5, pady= 5)
        
        self.canvas_1.pack()
        self.canvas_1.create_window(int(self.screen_width *0.1), int(self.screen_height*0.04), window= self.frame_cus_label, anchor= tk.N)
        self.canvas_1.create_window(int(self.screen_width *0.1), int(self.screen_height*0.08), window= self.frame_cus_infor, anchor= tk.N)
        self.canvas_1.create_line(int(self.screen_width *0.02), int(self.screen_height*0.28), int(self.screen_width *0.18), int(self.screen_height*0.28))
        self.canvas_1.create_window(int(self.screen_width *0.1), int(self.screen_height*0.32), window= self.frame_cus_add, anchor= tk.N)
        self.canvas_1.create_window(int(self.screen_width *0.1), int(self.screen_height*0.6), window= self.frame_cus_submit, anchor= tk.N)
        
    def Add_Customer(self) : 
        ID = int(self.ID.get())
        name = self.name.get()
        phone = self.phone.get()
        city = self.city.get()
        area = self.area.get()
        commune = self.commune.get() 
        description = self.description.get()
        
        cus = class_customer.Customer(ID, name, phone, city, area, commune, description)
        cus.Add_Customer()
        
        self.ID.set(class_customer.Get_ID())
        self.name.set('')
        self.phone.set('')
        self.city.set('')
        self.area.set('')
        self.commune.set('')
        self.description.set('') 
        self.flag_dome_1 = True
        self.window.destroy()
        
    
    def Window_Delete_Customer(self) : 
        self.window_1 = tk.Toplevel(self.root)
        self.window_1.geometry(f"{int(self.screen_width*0.2)}x{int(self.screen_height*0.1)}")
        self.canvas_2 = tk.Canvas(self.window_1, background= 'white', width= int(self.screen_width*0.2), height= int(self.screen_height*0.1))
        self.frame_delete = tk.Frame(self.window_1, background= 'white')
        self.flag_done_2 = False
        tk.Entry(self.frame_delete , textvariable= self.search_value_1, font= ('Arial', 15), background= 'white').pack(side= tk.LEFT,padx=5, pady= 5)
        tk.Button(self.frame_delete, text= 'Delete', font= ('Arial', 15), background= 'white', command= self.Delete_Customer).pack(side= tk.RIGHT, padx=5, pady= 5)
        
        
        self.canvas_2.pack()
        self.canvas_2.create_window(int(self.screen_width*0.1), int(self.screen_height*0.03), window= self.frame_delete, anchor= tk.N)
    def Delete_Customer(self): 
        id = int(self.search_value_1.get())
        class_customer.Delete_Customer(id)
        self.flag_done_2 = True
        self.search_value_1.set('')
        self.window_1.destroy()
        
    def Window_Change_Customer(self): 
        self.window_3 = tk.Toplevel(self.root)
        self.window_3.geometry(f"{int(self.screen_width*0.2)}x{int(self.screen_height*0.7)}")
        self.window_3.title("Cua so them nguoi dung moi")
        
        self.canvas_3 = tk.Canvas(self.window_3, width= int(self.screen_width*0.2), height= int(self.screen_height*0.7), background= 'white')
        
        self.frame_search_change = tk.Frame(self.canvas_3, background= 'white')
        self.frame_change_label = tk.Frame(self.canvas_3, background= 'white')
        self.frame_change_infor = tk.Frame(self.canvas_3, background= 'white')
        self.frame_change_add = tk.Frame(self.canvas_3, background= 'white')
        self.frame_change_submit  = tk.Frame(self.canvas_3, background= 'white')
        self.flag_dome_3 = False
        
        
        tk.Entry(self.frame_search_change , textvariable= self.search_value_1, font= ('Arial', 15), background= 'white').pack(side= tk.RIGHT,padx=5, pady= 5)
        tk.Button(self.frame_search_change, text= 'Search', font= ('Arial', 15), background= 'white', command= self.Find_Customer).pack(side= tk.LEFT, padx=5, pady= 5)
        
        tk.Label(self.frame_change_label, text= 'Thong tin khach hang ', font= ('Arial', 15), background= 'white', borderwidth= 0).pack()
        
        tk.Label(self.frame_change_infor, text= 'Ma khach hang', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5 )
        tk.Entry(self.frame_change_infor, textvariable= self.ID_search, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_change_infor, text= 'Ten khach hang', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_change_infor, textvariable= self.name, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_change_infor, text= 'So dien thoai', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_change_infor, textvariable= self.phone, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        

        tk.Label(self.frame_change_add, text= 'Tinh/ThanhPho', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5 )
        tk.Entry(self.frame_change_add, textvariable= self.city, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_change_add, text= 'Quan/Huyen', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_change_add, textvariable= self.area, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_change_add, text= 'Xa/Phuong/ThiTran', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_change_add, textvariable= self.commune, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        tk.Label(self.frame_change_add, text= 'Mo ta them', font= ('Arial', 15), background= 'white', borderwidth= 0).pack(padx= 5, pady= 5)
        tk.Entry(self.frame_change_add, textvariable= self.description, font= ('Arial', 15), background= 'white').pack(padx=5, pady= 5)
        
        tk.Button(self.frame_change_submit, text= 'Add', font= ('Arial', 15), background= 'white', command= self.Change_Customer).pack(side= tk.LEFT, padx=5, pady= 5)
        tk.Button(self.frame_change_submit, text= 'Exit', font= ('Arial', 15), background= 'white', command= self.window_3.destroy).pack(side= tk.RIGHT, padx=5, pady= 5)
        
        self.canvas_3.pack()
        self.canvas_3.create_window(int(self.screen_width *0.1), int(self.screen_height*0.02), window= self.frame_search_change, anchor= tk.N)
        self.canvas_3.create_window(int(self.screen_width *0.1), int(self.screen_height*0.08), window= self.frame_change_label, anchor= tk.N)
        self.canvas_3.create_window(int(self.screen_width *0.1), int(self.screen_height*0.12), window= self.frame_change_infor, anchor= tk.N)
        self.canvas_3.create_line(int(self.screen_width *0.02), int(self.screen_height*0.32), int(self.screen_width *0.18), int(self.screen_height*0.32))
        self.canvas_3.create_window(int(self.screen_width *0.1), int(self.screen_height*0.34), window= self.frame_change_add, anchor= tk.N)
        self.canvas_3.create_window(int(self.screen_width *0.15), int(self.screen_height*0.61), window= self.frame_change_submit, anchor= tk.N)
        
    def Find_Customer(self): 
        id = int(self.search_value_1.get())
        data = class_customer.Find_Cus_Add(id)
        data = data[0]
        self.ID_search.set(f'{data[0]}')
        self.name.set(f'{data[1]}')
        self.phone.set(f'{data[2]}')
        self.city.set(f'{data[3]}')
        self.area.set(f'{data[4]}')
        self.commune.set(f'{data[5]}')
        self.description.set(f'{data[6]}')
    
    def Change_Customer(self): 
        ID = int(self.ID_search.get())
        name = self.name.get()
        phone = self.phone.get()
        city = self.city.get()
        area = self.area.get()
        commune = self.commune.get() 
        description = self.description.get()
        
        cus = class_customer.Customer(ID, name, phone, city, area, commune, description)
        cus.Set_Customer()
        
        self.ID_search.set(class_customer.Get_ID())
        self.name.set('')
        self.phone.set('')
        self.city.set('')
        self.area.set('')
        self.commune.set('')
        self.description.set('') 
        self.flag_done_3 = True
        self.window_3.destroy()
    
    def get_done_1 (self): 
        return self.flag_dome_1 
    def get_done_2 (self): 
        return self.flag_dome_2
    def get_done_3 (self): 
        return self.flag_dome_3
    
# if __name__ == "__main__": 
#     root = tk.Tk()
#     Window_Customer(root)
#     root.mainloop()