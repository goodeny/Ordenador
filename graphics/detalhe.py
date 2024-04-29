from repository import Database
from tkinter import *

class Detalhe:
    def __init__(self):
        #for i in range(0, len(self.separete_data())):
            #print(self.separete_data()[i])
        pass
    
    def getInformation(self, id):
        self.db = Database()
        self.db.Connect()
        return self.db.separete_data()[id]