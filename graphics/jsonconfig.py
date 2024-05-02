from configpath import pathJson
import json
import getpass

def start():
    a = getpass.getpass('Database password [No password = ENTER]: ')
    if a == "":
        setPassword("")
    else:
        setPassword(a)

def getPassword():
    with open(pathJson(), 'r') as file:
        data = json.load(file)
    return data.get('bd_password')

def setPassword(new_password):
    with open(pathJson(), 'r') as file:
        data = json.load(file)
    data['bd_password'] = new_password
    with open(pathJson(), 'w') as file:
        json.dump(data, file)
