
import socket
from crc_code import encyrpt_data

HOST='127.0.0.1'
PORT=7011

#clientsocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
clientsocket= socket.socket() 
clientsocket.connect((HOST, PORT))
while True:
	st=input("enter string:")
	encrypted_msg=encyrpt_data(st)
	clientsocket.send(str(encrypted_msg).encode())
	ans=clientsocket.recv(1024).decode()
	print(ans)
clientsocket.close()
