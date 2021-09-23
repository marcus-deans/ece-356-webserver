# UDPPingerClient.py
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

# initialize counter to keep track of packet losses
lostCount = 0

# array of round-trip delays
resTimes = []

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

		# add to round trip delays
		resTimes.append(rtd)

		# print round trip delay and response message
		print(f"{count} received in {rtd}")
		print(f"Server Response: {msgFromServer[0]}")
	except:
		# print timeout message if client waits more than 2 sec
		print("Request timed out")

		# add to lost count
		lostCount += 1
	
	# increment packet number	
	count += 1

# calculate and print mean round trip delay (excluding packet losses)
meanTime = sum(resTimes)/len(resTimes)
print(f"Mean Response Time {meanTime}")

# print loss rate
print(f"Packet Loss Rate: {lostCount/15}")

# print minimum and maximum round trip delay
print(f"Minimum Response Time: {min(resTimes)}")
print(f"Maximum Response Time: {max(resTimes)}")