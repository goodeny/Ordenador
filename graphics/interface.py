from tkinter import *
from repository import Database
from detalhe import Detalhe
from plot import Program
from PIL import Image
import threading
import customtkinter

class Interface:
    def __init__(self):
        self.window = Tk()
        self.center(1200,500)
        self.window.resizable(0, 0)
        self.window.title('Ordenador - Graphics')
        self.window.config(bg='#1F1B30')
        self.create_frame_with_scrollbar()
        self.create()
        self.create_canvas_plot()
        self.create_cards()
        self.plot = False
    
    def center(self, w, h):
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        x = (width - w) // 2
        y = (height - h) // 2
        return self.window.geometry(f'{w}x{h}+{x}+{y}')

    def create_canvas_plot(self):
        self.canvas_plot = Canvas(self.window, bg='#1F1B30', width=500, height=400, highlightbackground="#1F1B30")
        self.canvas_plot.place(x=30, y=53)

    def create_frame_with_scrollbar(self):
        self.canvas = Canvas(self.window, bg='#1F1B30', width=500, height=430, highlightbackground="#1F1B30")
        self.canvas.place(x=800, y=40)
    
    def create(self):
        self.my_frame = customtkinter.CTkScrollableFrame(self.canvas, width=370, height=400, fg_color="#1F1B30")
        self.my_frame.pack()

    def create_cards(self):
        my_image = customtkinter.CTkImage(light_image=Image.open('assets/Rectangle 2.png'),
        dark_image=Image.open('assets/Rectangle 2.png'),
        size=(350,70)) # WidthxHeight
        self.background_card = PhotoImage(file='assets/Rectangle 2.png')
        self.backgorund_button = PhotoImage(file='assets/Group 1.png')
        self.repository = Database()
        self.repository.Connect()
        #print(len(self.repository.separete_data()))
        for i in range(0, len(self.repository.separete_data())):
            self.background_card = PhotoImage(file='assets/Rectangle 2.png')
            self.labelgeral = customtkinter.CTkLabel(self.my_frame, text="", image=my_image, bg_color='#1f1b30')
            self.labelgeral.pack(pady=10, padx=0)
            self.button = Button(self.labelgeral, 
                        image=self.backgorund_button,
                        activebackground="#363346",
                        bd=0,
                        bg='#363346',
                        command=lambda i=i: threading.Thread(target=self.getData, args=(i,)).start())
            self.button.place(x=50 , y=15)
            self.label = Label(self.labelgeral, 
                        text=f'Ordenado {i}', 
                        fg='white',
                        bg='#363346')
            self.label.place(x=170, y=25)
        
    def getData(self, id):
        if self.plot:
            self.canvas_plot.destroy()
            self.create_canvas_plot()
        self.plot = True
        self.create_canvas_plot()
        self.program = Program()
        self.detalhe = Detalhe()
        data = self.detalhe.getInformation(id)
        self.canvas_plot.delete("all")
        
        self.program.plot_graph(self.canvas_plot, data)
            
    def on_canvas_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
