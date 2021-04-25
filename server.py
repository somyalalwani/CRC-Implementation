from socket import *
from _thread import *
from crc_code import decrypt_data

def funct(client_connection):
	try:
		while True:
		
			st = client_connection.recv(1024).decode()
			if st=="":
				client_connection.sendall(str("Empty String recvd").encode())
			else:
				final_msg=decrypt_data(st)
				print(final_msg)
				if final_msg!="Recvd error":
					abc="Recvd successfully"
					client_connection.sendall(str(abc).encode())
				else:
					client_connection.sendall(str(final_msg).encode())
		client_connection.close()
	except:
		print("Tried receiving incorrect data")
	
	return



SERVER_HOST = '127.0.0.1'
SERVER_PORT = 7011 #server


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

while True:
	client_connection, client_address = server_socket.accept()
	start_new_thread(funct, (client_connection,))
client_connection.close()	
#server_socket.close()