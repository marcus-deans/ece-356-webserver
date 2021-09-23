# UDPHeartbeatServer.py
from socket import *
import time

# initialize client socket
clientSocket = socket(family=AF_INET, type=SOCK_DGRAM)

# throw exception if client does not receive response in 2 sec
clientSocket.settimeout(2)

# bind socket to address and port
clientSocket.bind((gethostbyname(gethostname()), 12001))

# initialize counter to keep track of packet number
count = 1

# server address
serverPort = (gethostbyname(gethostname()), 12000)

# while loop to run 15 times
while (count < 16):

	# time when packet is sent
	sendTime = time.time()

	# create message and encode into bytes
	msgToSend = f"{count} {sendTime}"
	byteMsg = str.encode(msgToSend)

	# send message to server
	clientSocket.sendto(byteMsg, serverPort)
	try:
		# wait for response from server
		msgFromServer = clientSocket.recvfrom(1024)

		# save receipt time
		recTime = time.time()

		# calculate round trip delay
		rtd = recTime - sendTime

		# print round trip delay and response message
		print(f"{count} received in {rtd}")
		print(f"Server Response: {msgFromServer[0]}")
	except:
		# print timeout message if client waits more than 2 sec
		print("Request timed out")

	# increment packet number
	count += 1