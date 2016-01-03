import socket

#Client socket
cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Get IP
ip=socket.gethostbyname(socket.gethostname())
#Port
port=11111

#Connect!

cli.connect((ip,port))

server_reply=cli.recv(65535)

print server_reply

cli.close()

