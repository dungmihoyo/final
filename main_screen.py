from tksheet import Sheet
import tkinter as tk
from PIL import Image, ImageTk 
from login_window import Login_Window

login = Login_Window(tk.Tk(), 'text')
class Main: 
    def __init__(self, window, title) :
        self.window = window 
        self.screen_height = self.window.winfo_screenheight()
        self.screen_width = self.window.winfo_screenwidth()
        self.flag = login.get_flag()
        self.window.title(title) 
        self.window.geometry(f"{int(self.screen_width)}x{int(self.screen_height)}")
        
        self.canvas_task = tk.Canvas(self.window, width= int(self.screen_width*0.2), height= int(self.screen_height), borderwidth= 3, highlightthickness= 0 , background='black') 
        self.canvas_information = tk.Canvas(self.window, width= int(self.screen_width*0.8), height= int(self.screen_height), borderwidth= 3, highlightthickness= 0 , background='blue') 
        
        self.frame_user = tk.Frame(self.canvas_task, borderwidth= 0, highlightthickness= 0, background= 'white')
        if(self.flag == 1) : 
            tk.Label(self.frame_user,  text = 'Admin', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.004),background='white').pack()
        if(self.flag == 2): 
            tk.Button(self.frame_user, text = 'Employee', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.004),background='white').pack()
        if(self.flag == 3): 
            tk.Button(self.frame_user, text = 'Manger', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.004),background='white').pack()
            
        self.frame_product = tk.Frame(self.canvas_task, borderwidth= 0, highlightthickness= 0, background= 'yellow')
        tk.Button(self.frame_product, text='Danh muc san pham', font=('Arial', 15), borderwidth= 0, highlightthickness= 0, foreground='red', width= int(self.screen_width*0.2), height= int(self.screen_height*0.002),background='white', command= self.window_information_employee).pack()
        
        
        self.canvas_task.pack(side= tk.LEFT) 
        self.canvas_information.pack(side= tk.RIGHT)
        self.canvas_task.create_window(150, 0, window = self.frame_user, anchor= tk.N)
        self.canvas_task.create_window(150, 100, window = self.frame_product, anchor= tk.N)
        
        print(self.screen_height, self.screen_width)
        
        
        
        
        if self.flag != 0 : 
            self.window.mainloop()
        
    def window_information_employee(self): 
        self.frame = tk.Frame(self.canvas_information)
        self.sheet_product = Sheet(self.frame, data=[[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(10)] for r in range(20)], width= int(self.screen_width*0.8), height= int(self.screen_height*0.8),show_row_index= False)
        self.sheet_product.headers(['ID', 'Hinh anh', 'Ten san pham', 'Gia tien', 'Ton kho', 'Dang cho', 'Dang van chuyen', 'Dang giu', 'Da ngung san xuat'])
        self.frame.pack()
        self.sheet_product.pack()

if __name__ == "__main__":
    Main(tk.Tk(), "UI")