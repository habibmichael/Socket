import socket

#Create IPV4 socket server
srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Get IP
srv_ip=socket.gethostbyname(socket.gethostname())


