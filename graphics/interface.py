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

        self.countinsort_time = []
        self.countinsort_size = []
        
        self.insertionsort_time = []
        self.insertionsort_size = []

        self.quicksort_time = []
        self.quicksort_size = []

        self.margesort_time = []
        self.margesort_size = []

        self.shellsort_time = []
        self.shellsort_size = []

    
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
        self.canvas.place(x=810, y=40)
    
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
            self.button_specify = Button(self.labelgeral, 
                        text="Expandir",
                        activebackground="#363346",
                        fg='white',
                        bd=0,
                        bg='#363346',
                        command=lambda i=i: threading.Thread(target=self.getData2, args=(i,)).start()
                        )
            self.button_specify.place(x=250 , y=25)

    def create_cards_counting(self, name, size, time):
        my_image_counting = customtkinter.CTkImage(light_image=Image.open(uploadImage('Rectangle 2.png')),
        dark_image=Image.open(uploadImage('Rectangle 2.png')),
        size=(350,70)) # WidthxHeight
        self.background_card_counting = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.backgorund_button_counting = PhotoImage(file=uploadImage('Group 1.png'))
        self.background_card_counting = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.labelgeral_counting = customtkinter.CTkLabel(self.my_frame, text="", image=my_image_counting, bg_color='#1f1b30')
        self.labelgeral_counting.pack(pady=10, padx=0)
        self.label_counting = Label(self.labelgeral_counting, 
                    text=name, 
                    fg='white',
                    bg='#363346')
        self.label_counting.place(x=170, y=25)
        self.button_counting = Button(self.labelgeral_counting, 
                        image=self.backgorund_button_counting,
                        activebackground="#363346",
                        bd=0,
                        bg='#363346',
                        command=lambda name=name, size=size, time=time: threading.Thread(target=self.instruct, args=(name,size,time,)).start())
        self.button_counting.place(x=50 , y=15)

    def create_cards_insertion(self, name, size, time):
        my_image_insertion = customtkinter.CTkImage(light_image=Image.open(uploadImage('Rectangle 2.png')),
        dark_image=Image.open(uploadImage('Rectangle 2.png')),
        size=(350,70)) # WidthxHeight
        self.background_card_insertion = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.backgorund_button_insertion = PhotoImage(file=uploadImage('Group 1.png'))
        self.background_card_insertion = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.labelgeral_insertion = customtkinter.CTkLabel(self.my_frame, text="", image=my_image_insertion, bg_color='#1f1b30')
        self.labelgeral_insertion.pack(pady=10, padx=0)
        self.label_insertion = Label(self.labelgeral_insertion, 
                    text=name, 
                    fg='white',
                    bg='#363346')
        self.label_insertion.place(x=170, y=25)
        self.button_insertion = Button(self.labelgeral_insertion, 
                        image=self.backgorund_button_insertion,
                        activebackground="#363346",
                        bd=0,
                        bg='#363346',
                        command=lambda name=name, time=time, size=size: threading.Thread(target=self.instruct, args=(name,size,time,)).start())
        self.button_insertion.place(x=50 , y=15)

    def create_cards_quick(self, name, size, time):
        my_image_quick = customtkinter.CTkImage(light_image=Image.open(uploadImage('Rectangle 2.png')),
        dark_image=Image.open(uploadImage('Rectangle 2.png')),
        size=(350,70)) # WidthxHeight
        self.background_card_quick = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.backgorund_button_quick = PhotoImage(file=uploadImage('Group 1.png'))
        self.background_card_quick = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.labelgeral_quick = customtkinter.CTkLabel(self.my_frame, text="", image=my_image_quick, bg_color='#1f1b30')
        self.labelgeral_quick.pack(pady=10, padx=0)
        self.label_quick = Label(self.labelgeral_quick, 
                    text=name, 
                    fg='white',
                    bg='#363346')
        self.label_quick.place(x=170, y=25)
        self.button_quick = Button(self.labelgeral_quick, 
                        image=self.backgorund_button_quick,
                        activebackground="#363346",
                        bd=0,
                        bg='#363346',
                        command=lambda name=name, time=time, size=size: threading.Thread(target=self.instruct, args=(name,size,time,)).start())
        self.button_quick.place(x=50 , y=15)

    def create_cards_marge(self, name, size, time):
        my_image_marge = customtkinter.CTkImage(light_image=Image.open(uploadImage('Rectangle 2.png')),
        dark_image=Image.open(uploadImage('Rectangle 2.png')),
        size=(350,70)) # WidthxHeight
        self.background_card_marge = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.backgorund_button_marge = PhotoImage(file=uploadImage('Group 1.png'))
        self.background_card_marge = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.labelgeral_marge = customtkinter.CTkLabel(self.my_frame, text="", image=my_image_marge, bg_color='#1f1b30')
        self.labelgeral_marge.pack(pady=10, padx=0)
        self.label_marge = Label(self.labelgeral_marge, 
                    text=name, 
                    fg='white',
                    bg='#363346')
        self.label_marge.place(x=170, y=25)
        self.button_marge = Button(self.labelgeral_marge, 
                        image=self.backgorund_button_marge,
                        activebackground="#363346",
                        bd=0,
                        bg='#363346',
                        command=lambda name=name, time=time, size=size: threading.Thread(target=self.instruct, args=(name,size,time,)).start())
        self.button_marge.place(x=50 , y=15)

    def create_cards_shell(self, name, size, time):
        my_image_shell = customtkinter.CTkImage(light_image=Image.open(uploadImage('Rectangle 2.png')),
        dark_image=Image.open(uploadImage('Rectangle 2.png')),
        size=(350,70)) # WidthxHeight
        self.background_card_shell = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.backgorund_button_shell = PhotoImage(file=uploadImage('Group 1.png'))
        self.background_card_shell = PhotoImage(file=uploadImage('Rectangle 2.png'))
        self.labelgeral_shell = customtkinter.CTkLabel(self.my_frame, text="", image=my_image_shell, bg_color='#1f1b30')
        self.labelgeral_shell.pack(pady=10, padx=0)
        self.label_shell = Label(self.labelgeral_shell, 
                    text=name, 
                    fg='white',
                    bg='#363346')
        self.label_shell.place(x=170, y=25)
        self.button_shell = Button(self.labelgeral_shell, 
                        image=self.backgorund_button_shell,
                        activebackground="#363346",
                        bd=0,
                        bg='#363346',
                        command=lambda name=name, time=time, size=size: threading.Thread(target=self.instruct, args=(name,size,time,)).start())
        self.button_shell.place(x=50 , y=15)

    def getData(self, id):     
        if self.plot:
            self.canvas_plot.destroy()
            self.create_canvas_plot()
            self.plot = False
        self.plot = True
        self.create_canvas_plot()
        self.program = Program()
        self.detalhe = Detalhe()
        data = self.detalhe.getInformation(id)
        print(data)
        self.canvas_plot.delete("all")
        self.program.plot_graph(self.canvas_plot, data)
    
    def getData2(self, id):
        self.create_back_button()
        g_id = id + 1
        self.canvas.destroy()
        self.create_frame_with_scrollbar()
        self.create()
        self.detalhe = Detalhe()

        try:
            self.countinsort_time.clear()
            self.countinsort_size.clear()

            self.insertionsort_time.clear()
            self.insertionsort_size.clear()

            self.quicksort_time.clear()
            self.quicksort_size.clear()

            self.margesort_time.clear()
            self.margesort_size.clear()

            self.shellsort_time.clear()
            self.shellsort_size.clear()
        except:
            pass

        for i in range(0, 5):
            self.countinsort_size.append(self.detalhe.getInformation2(id)[i][2])
            self.countinsort_time.append(self.detalhe.getInformation2(id)[i][3])
    
        for i in range(5, 10):
            self.insertionsort_size.append(self.detalhe.getInformation2(id)[i][2])
            self.insertionsort_time.append(self.detalhe.getInformation2(id)[i][3])

        for i in range(10, 15):
            self.quicksort_size.append(self.detalhe.getInformation2(id)[i][2])
            self.quicksort_time.append(self.detalhe.getInformation2(id)[i][3])

        for i in range(15, 20):
            self.margesort_size.append(self.detalhe.getInformation2(id)[i][2])
            self.margesort_time.append(self.detalhe.getInformation2(id)[i][3])

        for i in range(20, 25):
            self.shellsort_size.append(self.detalhe.getInformation2(id)[i][2])
            self.shellsort_time.append(self.detalhe.getInformation2(id)[i][3])

        self.create_cards_counting('Counting Sort', self.countinsort_size, self.countinsort_time)
        self.create_cards_insertion('Insertion Sort', self.insertionsort_size, self.insertionsort_time)
        self.create_cards_quick('Quick Sort', self.quicksort_size, self.quicksort_time)
        self.create_cards_marge('Marge Sort', self.margesort_size, self.margesort_time)
        self.create_cards_shell('Shell Sort', self.shellsort_size, self.shellsort_time)

    def instruct(self, name, size, time):
        self.canvas_plot.delete("all")
        if self.plot:
            self.canvas_plot.destroy()
            self.create_canvas_plot()
        self.plot = True
        self.create_canvas_plot()
        self.program = Program()
        self.detalhe = Detalhe()


        self.canvas_plot.delete("all")
        self.program.plot_graph2(self.canvas_plot, size, time)
        
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

    def create_back_button(self):
        self.background_back_button = PhotoImage(file=uploadImage('Group 5.png'))
        self.back_button = Button(self.window, 
                                image=self.background_back_button, 
                                activebackground="#1f1b30", 
                                bg='#1f1b30',
                                bd = 0,
                                command=lambda: threading.Thread(target= self.back_function).start())
        self.back_button.place(x=810, y=453)

    def back_function(self):
        self.back_button.destroy()
        self.canvas.destroy()
        self.create_frame_with_scrollbar()
        self.create()
        self.create_cards()
        
