# UDPHeartbeatServer.py

import random
import time
from socket import *

# initialize server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# sets timeout to 5 seconds
serverSocket.settimeout(5)

# binds socket to port 12000
serverSocket.bind((gethostbyname(gethostname()), 12000))

# Variable to keep track of next expected packet number
expectedNum = 1

# Lost packet counter
lost = 0

# Infinite loop to listen for packets
while True:
	try:
		# wait for 5 seconds to receive a packet
		message, address = serverSocket.recvfrom(1024)

		# when packet received, save time
		recTime = time.time()

		# decode message from bytes to string
		msg_decoded = message.decode()

		# split msg into array [seq_number, time]
		contents = msg_decoded.split()

		# convert time from string to float
		sendTime = float(contents[1])

		# convert packet number to int
		packNum = int(contents[0])

		# Code to print out if packets are lost, and which packets were lost
		if packNum != expectedNum:
			if (packNum - expectedNum) == 1:
				print(f"Packet {expectedNum} lost")
			else:
				print(f"Packets {expectedNum} through {packNum - 1} were lost")
			lost += packNum - expectedNum

		# increment expected packet number
		expectedNum = packNum + 1

		# calculate one way packet delay
		diff = recTime - sendTime

		# print messages with packet number, one-way delay, and message
		print(f"Packet {int(contents[0])} received with contents: {msg_decoded}")
		print(f"Packet {int(contents[0])} sent in {diff}")

		# send response message to server
		serverSocket.sendto(message, address)
	except:
		# if recvfrom times out after 5 sec, we assume the client is done sending packets
		"Client Packets Stopped"
		break

# print number of packets lost
print(f"{lost} packets lost")

