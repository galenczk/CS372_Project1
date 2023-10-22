# Date: October 21, 2023
# Adapted from Computer Networking, A Top-Down Approach
# Authors: James F. Kurose & Keith W. Ross
# Purpose: TCP client socket in Python
from socket import *

# Server hostname and port to connect to
serverName = "gaia.cs.umass.edu"
serverPort = 80
# Create a socket to connect to the server using IPv4 and TCP.
clientSocket = socket(AF_INET, SOCK_STREAM)
# Attempt to connect to server using socket.
clientSocket.connect((serverName, serverPort))
# Payload contains GET Request.
payload = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
# Send payload to server using socket connection.
clientSocket.send(payload.encode())


# Date: October 21, 2023
# Adapted from: "https://www.geeksforgeeks.org/python-write-bytes-to-file/"
# Purpose: How to write bytes to data object in Python
# Response is an empty byte object that the response will be written to.
response = b""

# Loop to write bytes from HTTP Response to response.
while True:
    new = clientSocket.recv(2048)
    # When clientSocket is not longer receiving, end loop.
    if not new:
        break
    # Write any new bytes to response.
    response += new

# Print response and close clientSocket.
print(response)
clientSocket.close()
