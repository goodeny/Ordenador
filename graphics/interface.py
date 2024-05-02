from tkinter import *
from repository import Database
from detalhe import Detalhe
from plot import Program
from PIL import Image
from configpath import uploadImage
import threading
import customtkinter
import threading
import time
import os

class Interface:
    def __init__(self):
        self.window = Tk()
        self.center(1200,500)
        self.window.resizable(0, 0)
        self.window.title('Ordenador - Graphics')
        self.window.config(bg='#1F1B30')
        self.repository = Database()
        self.repository.Connect()
        self.create_frame_with_scrollbar()
        self.create()
        self.create_canvas_plot()
        self.create_cards()
        self.create_update_label()
        
        threading.Thread(target=self.updateList).start()
        self.plot = False
        self.qnt = 0
    
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
        

        my_image = customtkinter.CTkImage(light_image=Image.open(uploadImage('Rectangle 2.png')),
        dark_image=Image.open(uploadImage('Rectangle 2.png')),
        size=(350,70)) # WidthxHeight
        self.background_card = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.backgorund_button = PhotoImage(file=uploadImage('Group 1.png'))
        self.lists = len(self.repository.separete_data())
        #print(len(self.repository.separete_data()))
        for i in range(0, self.lists):
            self.background_card = PhotoImage(file=uploadImage('Rectangle 2.png'))
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
                        text=f'Gráfico {i+1}', 
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

    def create_update_label(self):
        self.update_label = Label(self.window, text='Dados atualizados!', bg='#1f1b30', fg='green', font='19')
        self.update_label.place(x=940, y=460)

    def updateList(self):
        self.q = 0
        while True:
            self.bd = Database()
            self.bd.Connect()
            time.sleep(2)
            bd = int(len(self.bd.getAll()))/5
            interface = self.lists
            if interface < bd:
                self.update_label.config(text='Atualizando...', fg='orange')
                self.canvas.delete()
                self.create_frame_with_scrollbar()
                self.my_frame.destroy()
                self.create()
                self.create_cards()
                self.lists = bd
            else:
                self.update_label.config(text='Dados atualizados!', fg='green')