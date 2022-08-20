import socket

serverIP=input("server/person ip: ")
serverPORT=input("server/person port: ")
localPORT=input("your port: ")

s = socket.socket()
s.connect((serverIP, serverPORT))
while True:
    print(s.recv(1024))
s.close()