# UDPHeartbeatServer.py

import random
import time
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)

# sets timeout to 5 seconds
serverSocket.settimeout(5)

#binds socket to port 12000
serverSocket.bind((gethostbyname(gethostname()), 12000))

while True:
	rand = random.randint(0,10)
	try:
		message, address = serverSocket.recvfrom(1024)
		recTime = time.time()

		print(f"{i} received with contents: {message}")
		msg_decoded = message.decode()
		contents = msg_decoded.split()
		sendTime = float(contents[1])

		diff = recTime - sendTime

		print(f"Packet {contents[0]} sent in {diff}")
		if rand < 3:
			continue

		serverSocket.sendto(message, address)
	except:
		print("Packet Loss")

	i += 1