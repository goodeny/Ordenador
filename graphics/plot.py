from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Program:
    def __init__(self):
        self.figure = None
        self.canvas_widget = None
    
    def plot_graph(self, canvas, data):
        canvas.delete("all")
        
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        if self.figure is not None:
            self.figure.clear()

        d_time = []
        d_size = []
        for i in data:
            d_time.append(i[1])
            d_size.append(i[2])

        time = d_time
        size = d_size

        figsize = (canvas_width / 65, canvas_height / 100)

        if self.figure is None:
            self.figure = Figure(figsize=figsize, dpi=100)
            plot = self.figure.add_subplot(111)
        else:
            plot = self.figure.add_subplot(111)

        plot.plot(time, size)
        try:
            if self.canvas_widget is None:
                self.canvas_widget = FigureCanvasTkAgg(self.figure, master=canvas)
                self.canvas_widget.draw()
                self.canvas_widget.get_tk_widget().pack(side='top', fill='both', expand=1)
            else:
                self.canvas_widget.draw()
        except:
            pass