from tkinter import *
from repository import Database
from detalhe import Detalhe
import threading

class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('1000x500')
        self.window.resizable(0, 0)
        self.create_frame_with_scrollbar()
        #self.create_buttons()
        self.create_canvas_plot()
        self.create_cards()
    
    def create_canvas_plot(self):
        self.canvas_plot = Canvas(self.window, bg='green', width=400, height=400)
        self.canvas_plot.place(x=30, y=40)

    def create_frame_with_scrollbar(self):
        self.canvas = Canvas(self.window, bg='red', height=400, width=500)
        self.canvas.place(x=450, y=40)
        # Adiciona um scrollbar vertical associado ao canvas
        self.scrollbar = Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.scrollbar.place(x=960, y=40, height=400)
        # Configura o canvas para rolar com o scrollbar
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        # Configura o canvas para ajustar o tamanho do frame
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        # Adiciona o frame dentro do canvas
        self.frame = Frame(self.canvas, bg='red')
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

    def create_buttons(self):
        for _ in range(20):
            button = Button(self.frame, text='AAAAAAAAAAAA', font='arial 30')
            button.pack()

    def create_cards(self):
        self.repository = Database()
        self.repository.Connect()
        print(len(self.repository.separete_data()))
        for i in range(0, len(self.repository.separete_data())):
            self.labelgeral = Label(self.frame, height=3, width=30)
            self.labelgeral.pack(pady=10)
            self.button = Button(self.labelgeral, command=lambda i=i: threading.Thread(target=self.getData, args=(i,)).start())
            self.button.place(x= 0 , y=0)
            self.label = Label(self.labelgeral, text=f'Ordenado {i}')
            self.label.place(x = 40, y=0)
    
    def getData(self, id):
        self.detalhe = Detalhe()
        data = self.detalhe.getInformation(id)
        print(data)
            
    def on_canvas_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    interface = Interface()
    interface.window.mainloop()
