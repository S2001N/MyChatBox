import socket
import threading
import time

# Define Your local IP Address...
addr  = "127.0.0.1"
port = 5556

# For sending message...
print("Enter quit for exit from the chat : ")
def send(con):
    while(True):
        msg = input()
        if(msg == "quit"):
        	print("Server Terminated from the chat.")
        	break
        con.send(msg.encode())

# For receiving message...
def recieve(con):
    while(True):
        data = con.recv(1024).decode()
        if(data == "quit"):
        	break
        print("(Client Side):---> ", data)

# Define the network parameters that are used in the network socket...  
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((addr, port))
print("Server is waiting for connections...")
serverSocket.listen(1)

# Accept the connection address (IP and Connection ID) 
con, clientAddr = serverSocket.accept()
print("Connected with IP Address:-> ", clientAddr)

# Now, create two threads for communication simultaneously...
# This is for sending...
sendThread = threading.Thread(target=send, args=(con, ))
sendThread.start()

# This is for receiving...
recThread = threading.Thread(target=recieve, args=(con, ))
recThread.start()

sendThread.join()
recThread.join()

con.close()
serverSocket.close()
