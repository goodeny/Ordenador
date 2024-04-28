import matplotlib.pyplot as plt
from repository import Database

class Program:
    def __init__(self):
        self.database = Database()
        self.database.Connect()
        self.plot()

    def plot(self):
        xpoints = []
        for i in self.database.getSize():
            xpoints.append(f"{str(i)} Bytes")
        ypoints = self.database.getTime()
        xpoints.reverse()
        ypoints.reverse()
        plt.plot(xpoints, ypoints)
        plt.xlabel('Size')
        plt.ylabel('Time')
        plt.title('Gráfico de Linha: Size vs. Time')
        plt.show()

if __name__ == "__main__":
    program = Program()