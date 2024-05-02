import os
from jsonconfig import start
os.system('pip install -r requirements.txt')
start()
from interface import Interface
interface = Interface()
interface.window.mainloop()
