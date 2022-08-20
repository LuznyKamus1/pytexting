import socket

serverIP=input("server/person ip: ")
serverPORT=input("server/person port: ")
localPORT=input("your port:")
buffersize=1024

Sock = socket.socket(family=socket.AF_inet, type=socket.STREAM); sock.bind((socket.gethostbyname_ex(socket.getfqdn())[2][0], localPORT))