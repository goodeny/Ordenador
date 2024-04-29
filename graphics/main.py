import os
os.system('pip install -r requirements.txt')
from interface import Interface
interface = Interface()
interface.window.mainloop()