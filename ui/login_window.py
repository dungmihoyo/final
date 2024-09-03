from tksheet import Sheet
import tkinter as tk 
import sys
sys.path.append("./class")



from class_login import Login_Information
from PIL import Image, ImageTk


class Login_Window(Login_Information): 
    def __init__(self, window, title):
        
        self.window = window
        self.window.title(title)
        
        self.ID = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        self.flag = 0
        self.flag_server = False 
        
        self.data_employee = None
        
        self.screen_height = self.window.winfo_screenheight()
        self.screen_width = self.window.winfo_screenwidth()
        self.window.geometry(f"{int(self.screen_width*0.3)}x{int(self.screen_height*0.4)}")
        
        self.canvas_login = tk.Canvas(self.window, width= int(self.screen_width*0.3), height= int(self.screen_height*0.2), borderwidth= 0, highlightthickness= 0 )
        self.layer_title = tk.LabelFrame(self.canvas_login, borderwidth=0)
        tk.Label(self.layer_title, text = "Ung dung quan li\n kho hang, ban hang", font= ("Arial", 20)).pack() 

        self.frame_option = tk.Frame(self.canvas_login)
        option_list = ['Client', 'Employee', 'Manager']
        self.select_option = tk.StringVar(value=option_list[0])
        tk.Label(self.frame_option, text="Sever : ", font=("Arial", 15)).pack(side=tk.LEFT, padx= 45)
        tk.OptionMenu(self.frame_option, self.select_option, *option_list, command= lambda option: self.login_form(self.select_option)).pack(side = tk.RIGHT, padx= 15)
        
        self.canvas_entry = tk.Canvas(self.window, width= int(self.screen_width*0.2), height= int(self.screen_height*0.1), borderwidth= 0, highlightthickness= 0)
        
        self.layer_frame = tk.Frame(self.canvas_entry, borderwidth= 0) 
        tk.Entry(self.layer_frame, textvariable= self.ID, width= 20, borderwidth= 0, font= ("Arial", 15)).pack( pady= 5)
        tk.Entry(self.layer_frame, textvariable= self.username, width= 20, borderwidth= 0, font= ("Arial", 15)).pack( pady= 5)
        tk.Entry(self.layer_frame, textvariable= self.password, width= 20, borderwidth= 0, font= ("Arial", 15), show="*").pack( pady= 5)
        
        self.layer_label = tk.Frame(self.canvas_entry, borderwidth= 0) 
        tk.Label(self.layer_label, text = "ID", font=("Arial", 15)).pack(pady= 3)
        tk.Label(self.layer_label, text = "Username", font=("Arial", 15)).pack(pady= 3)
        tk.Label(self.layer_label, text = "Password", font=("Arial", 15)).pack(pady= 3)
        
        self.canvas_button = tk.Canvas(self.window, width= int(self.screen_width*0.2), height= int(self.screen_height*0.1), borderwidth= 0, highlightthickness= 0)
        self.layer_button = tk.Frame(self.canvas_button, borderwidth= 0) 
        tk.Button(self.layer_button, text = 'Connect', width= 30, command= self.check_information).pack(side = tk.RIGHT, padx= 10)
        
        self.canvas_login.pack()
        self.canvas_entry.pack()
        self.canvas_button.pack()
        
        self.canvas_login.create_window(300, 80, window= self.layer_title, anchor= tk.N)
        self.canvas_login.create_line(100, 150, 500, 150)
        self.canvas_login.create_window(200, 180, window= self.frame_option, anchor= tk.N)
        
        self.canvas_button.create_window(250, 0, window= self.layer_button, anchor= tk.N)
        
        self.window.mainloop()    
        
    def login_form(self, option): 
        value = option.get()
        if value == 'Client':
            self.flag_server = False
        if value == 'Employee' or value == 'Manager':
            self.flag_server = True 
            
        if self.flag_server == True: 
            self.canvas_entry.create_window(50, 0, window= self.layer_label, anchor= tk.N)
            self.canvas_entry.create_window(250, 0, window= self.layer_frame, anchor= tk.N)
          
        if self.flag_server == False: 
            self.canvas_entry.delete('all')
    def get_flag(self): 
        return self.flag        
    def get_profile(self): 
        return self.data_employee
    
    def check_information(self): 
        position = self.select_option.get()
        if position == 'Client': 
            self.flag = 1
            self.window.destroy()
        
        if position == 'Employee': 
            ID = self.ID.get()
            username = self.username.get()
            password = self.password.get()
            print(ID, username, password, position)
            login = Login_Information(int(ID), f'{username}', f'{password}', f'{position}')
            if login.Check_Information() == True : 
                self.flag = 2
                self.data_employee= login.Find_profile_employee()
                self.window.destroy()
            if login.Check_Information() == False : 
                pass 
            
        if position == 'Manager': 
            ID = self.ID.get()
            username = self.username.get()
            password = self.password.get()
            print(ID, username, password, position)
            login = Login_Information(int(ID), f'{username}', f'{password}', f'{position}')
            if login.Check_Information() == True : 
                self.flag = 3
                self.data_employee= login.Find_profile_employee()
                self.window.destroy()
            if login.Check_Information() == False : 
                pass          

# if __name__ == "__main__":
#     app = Login_Window(tk.Tk(), "test")
#     print(app.get_flag())