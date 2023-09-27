import socket
import threading
import time

# Your local IP address...
addr = "127.0.0.1"
port = 5556

# For Sending message...
print("Enter quit for exit from the chat : ")
def send(sock):
    while(True):
        msg = input()
        if(msg == "quit"):
        	print("Client terminated from the chat.")
        	break
        sock.send(msg.encode())

# For receiving message...
def recieve(sock):
    while(True):
        data = sock.recv(1024).decode()
        if(data == "quit"):
        	break
        print("(Server Side):---> ", data)

# Define the network parameters that are used in the network socket...  
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind your IP address with your port number that you are using...
clientSocket.connect((addr, port))
print("Connected with server Successfully...")

# Now, create two threads for communication simultaneously...
# This is for sending...
sendThread = threading.Thread(target=send, args=(clientSocket, ))
sendThread.start()

# This is for receiving...
recThread = threading.Thread(target=recieve, args=(clientSocket, ))
recThread.start()

sendThread.join()
recThread.join()


clientSocket.close()
