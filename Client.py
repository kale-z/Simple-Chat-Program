# Client Side:

import socket
import threading

# As long as the client is connected, he can Transmit messages
# Otherwise, he can't due to lost connection
def Transmission():
    while True:
        try:
            Message = str(input('Me > '))
            clientsocket.send(Message.encode('ascii'))
        except:
            print('Sorry! The server has been disconnected. \nYou will be kicked out!')
            break

# As long as the client is connected, he can Receive messages
# Otherwise, he can't due to lost connection
def Reception():
    while True:
        try:
            sen_name = clientsocket.recv(1024).decode('ascii')
            data = clientsocket.recv(1024).decode('ascii')

            print('\n' + str(sen_name) + ' > ' + str(data))
        except:
            print('Server has been disconnected')
            break

#=============================================================================================

# TCP Connection:

# Creating a socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establishing a connection
HOST = socket.gethostname() # The Localhost IP Adress
PORT = 4444

# After establishing connection, client enters a username
# then will be able to chat due to available threads
try:
    clientsocket.connect( (HOST, PORT) )
    print('Connected to remote host...')
    Username = str(input('Enter your name to enter the chat > '))
    clientsocket.send(Username.encode('ascii')) # Entering the chat

    SendThread = threading.Thread(target = Transmission)
    SendThread.start() # Creating a thread for sending messages

    ReceiveThread = threading.Thread(target = Reception)
    ReceiveThread.start() # Creating a thread for sending messages
except:
    print("There is no available server!")

#=============================================================================================
#=============================================================================================
