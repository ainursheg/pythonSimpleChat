import socket, time   # importing libraries

host = socket.gethostbyname(socket.gethostname()) #get ip
port = 9090 

clients = [] # Array for clients

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # TCP/IP
s.bind((host, port)) # Raise the server

quit = False 
print("[ Server Started ]")

while not quit:
	try:
		data, address = s.recvfrom(1024) # 1024 - size of data in bytes

		if address not in clients:
			clients.append(address)

		itsatime = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

		print("[" + address[0] + "]=[" + str(address[1]) + "]=[" + itsatime + "]/", end = "")
		print(data.decode("utf-8"))

		for client in clients:
			if address != client:
				s.sendto(data, client)
	except:
		print("\n[ Server Stopped ]")
		quit = True
s.close()