import socket
import json

s = socket.socket()
dict= {
   "request": "subscribe",
   "port": 3000,
   "name": "fun_name_for_the_client",
   "matricules": ["12345", "67890"]}


try :
    s.connect((adresse, portMach))
    s.send(dict)


except: 
    s.close()

    
