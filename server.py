import socket

s=socket.socket()
port=input("your port: ")
serverNAME=input("server name: ")
s.bind((socket.gethostname(), port))

s.listen(5)
while True:
    c, addr = s.accept()
    print(addr, " connected")
    c.send("you connected to ", serverNAME)