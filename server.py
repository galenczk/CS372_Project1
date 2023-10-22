# Date: October 21, 2023
# Adapted from Computer Networking, A Top-Down Approach
# Authors: James F. Kurose & Keith W. Ross
# Purpose: TCP server socket in Python
from socket import *

# Server hostname and port.
serverName = "127.0.0.1"
serverPort = 1033

# Create a serverSocket using the hostname and port above.
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind socket to hostname (IP Address) and port to start listening for
# requests.
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("The server is now ready to receive...")

# A loop to keep the socket open to new connections over time.
while True:
    # When a new connection comes in, create a new socket to handle it.
    connectionSocket, addr = serverSocket.accept()
    # Receive the request from the client
    request = connectionSocket.recv(2048).decode()

    # Print the request as it is received.
    print(request)

    # Prepare a response payload to respond to the client.
    data = """HTTP/1.1 200 OK\r\n"\
 "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
 "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"""

    # Send the response payload back to the client.
    connectionSocket.send(data.encode())
    # Close the connectionSocket (serverSocket is still open for subsequent
    # requests)
    connectionSocket.close()
