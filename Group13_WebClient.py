# import socket module
from socket import *
import sys  # in order to terminate program

clientSocket = socket(AF_INET, SOCK_STREAM)  # create client socket
PACKET_SIZE = 1024  # specify packet size of 1KB

server_host = sys.argv[1]  # the server hostname is the first argument
server_port = int(sys.argv[2])  # the server port name is the second argument
filename = sys.argv[3]  # the filename to be retrieved is the third argument

try:
    # Establish the connection by connecting client socket to specified server socket
    clientSocket.connect((server_host, server_port))
    sendMessage = 'GET /' + filename  # Create appropriately formatted GET request to file
    clientSocket.send(sendMessage.encode())  # Send GET request to server
    while True:  # While there is file information being returned
        data = clientSocket.recv(PACKET_SIZE)  # Receive up to 1KB in information
        print(data.decode(), end='')  # decode the data and add ending so it appears correctly
except Exception as e:
    print(e)  # if there is error in connection or in file decoding
clientSocket.close()  # close the client socket
sys.exit()  # system exist
