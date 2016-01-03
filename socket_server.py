import socket

#Create IPV4 socket server
srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Get IP
srv_ip=socket.gethostbyname(socket.gethostname())

#Define Port
srv_port=1111

#Bind Port & IP
srv.bind((srv_ip,srv_port))

#Listen from potential clients #argument contains max number of queued conn
srv.listen(2)

#Prepare server for accepting connections
client,ip=srv.accept()

#Welcome message when client joins server
client.send("Hi welcome to this server!")

