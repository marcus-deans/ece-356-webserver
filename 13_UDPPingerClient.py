# UDPPingerServer.py
from socket import *
import time

clientSocket = socket(family=AF_INET, type=SOCK_DGRAM)

clientSocket.settimeout(2)
print(gethostbyname(gethostname()))
clientSocket.bind((gethostbyname(gethostname()), 12001))

bufferSize = 1024
count = 1

lostCount = 0
resTimes = []

serverPort = (gethostbyname(gethostname()), 12000)

while (count < 16):
	sendTime = time.time()
	timeStr = time.localtime(sendTime)
	msgToSend = f"{count} {sendTime}"

	byteMsg = str.encode(msgToSend)
	clientSocket.sendto(byteMsg, serverPort)
	try:
		msgFromServer = clientSocket.recvfrom(bufferSize)
		recTime = time.time()

		rtd = recTime - sendTime
		resTimes.append(rtd)

		print(f"{count} received in {rtd}")
		msg = f"Server Response: {msgFromServer[0]}"
		print(msg)
	except:
		lostCount += 1
		print("Request timed out")
		
	count += 1

print("no?")
meanTime = sum(resTimes)/len(resTimes)

print(f"Packet Loss Rate: {lostCount/15}")
print(f"Minimum Response Time: {min(resTimes)}")
print(f"Maximum Response Time: {max(resTimes)}")
print(f"Mean Response Time {meanTime}")