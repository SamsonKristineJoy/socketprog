#import
import socket
#create socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#establish connection to client1.py
s.bind(socket.gethostname(), 1025)
s.listen(5)

while True:
    clt, adr=s.accept()
    print(f"connection to {adr} established")
    clt.send(bytes("Socket Programming in Python", "utf-8"))
    clt.close()