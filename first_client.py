# Date: October 21, 2023
# Adapted from Computer Networking, A Top-Down Approach
# Authors: James F. Kurose & Keith W. Ross
from socket import *

# Server hostname and port to connect to.
serverName = "gaia.cs.umass.edu"
serverPort = 80
# Create a socket using IPv4 and TCP.
clientSocket = socket(AF_INET, SOCK_STREAM)
# Attempt to connect socket to server hostname and port.
clientSocket.connect((serverName, serverPort))
# Payload contains GET request.
payload = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
# Send GET request to server.
clientSocket.send(payload.encode())

# Receive response from server.
response = clientSocket.recv(2048)

# Print response and close socket.
print(response)
clientSocket.close()
