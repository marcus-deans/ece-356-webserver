# import socket module
from socket import *
import sys  # in order to terminate program

serverSocket = socket(AF_INET, SOCK_STREAM)  # Create server socket
# Prepare a server socket
hostname = gethostname()  # Determine and save the localhost
port = 24000  # Arbitrary port number
serverSocket.bind((hostname, port))  # Create socket on local machine with selected port number
serverSocket.listen(5)  # Allow up to 5 clients in queue

# Print out URL for convenience
print('The Web server URl for this server is http://%s:%d/HelloWorld.html' % (hostname, port))
PACKET_SIZE = 1024
while True:
    print('Ready to serve...')
    # Establish the connection by accepting incoming request
    connectionSocket, connectionAddress = serverSocket.accept()
    try:
        message = connectionSocket.recv(PACKET_SIZE).decode()  # Receive an incoming message up to 1KB
        filename = message.split()[1]  # Split the message and obtain only the GET request
        f = open(filename[1:])  # Obtain the file specified in GET, less the first '/'
        outputdata = f.read()  # Read the file
        successMessage = 'HTTP/1.0 200 OK\n\n'  # Create appropriately formatted success message
        connectionSocket.sendall(successMessage.encode())  # Send one HTTP header line into socket
        # Send the content of the request file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        print('File sent')
    except IOError:
        errorMessage = 'HTTP/1.0 404 Not Found\n\n404 Not Found'  # Create appropriate formatted 404 Not Found message
        connectionSocket.sendall(errorMessage.encode())  # Send response message for file not found
        print('Unknown file request')
    connectionSocket.close()  # Close client socket
    serverSocket.close()  # Close server socket
    sys.exit()  # Terminate the program after sending the corresponding data
