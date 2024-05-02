import os
from configpath import requirements
from jsonconfig import start
os.system(f'pip install -r {requirements()}')
start()
from interface import Interface
interface = Interface()
interface.window.mainloop()
