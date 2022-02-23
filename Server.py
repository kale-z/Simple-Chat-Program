# Server Side:

from tkinter import *
import os
import socket
import threading

Interface2 = Tk()

def closing():
    Interface2.destroy()
    os._exit(0)


Interface2.title("History Logs")

screen = Listbox(Interface2)

# logs = INSERT(screen)
scrollbar = Scrollbar(Interface2, orient="vertical", command=screen.yview)
button = Button(Interface2, text="Close", font="Arial 13", command=closing)

scrollbar.pack(side="right", fill="y")
screen.pack(side="left", fill="both", expand=True)

scrollbar.pack(side="right", fill="y")
screen.pack(side="left", fill="both", expand=True)
button.pack()
button.place(x=319, y=10)

Interface2.maxsize(400, 300)
Interface2.minsize(400, 300)



Clients = [] # a list to reserve places for connected clients to be served

# After the connection have been established, the server receives the username
# and adds him to clients list. Then, announces his connection and create a thread to receive his messages
i=2
def Connection():
    global i
    while True:
        clientsocket, addr = serversocket.accept()
        Username = clientsocket.recv(1024).decode('ascii')
        Clients.append( (Username, clientsocket) )
        screen.insert(i,'%s is now connected' % Username)
        ClientThread = threading.Thread(target = ReceiveClientsMessages, args=[Username, clientsocket])
        ClientThread.start()
        i+=1

# Using Nickname and client's IP adress, the server receives clients' messages
# announces his speaking and broadcast those messages. Also, it announces user's disconnection
def ReceiveClientsMessages(Username, clientsocket):
    global i
    while True:
        try:
            Message = clientsocket.recv(1024).decode('ascii')
            if Message:
                screen.insert(i, "{0} spoke".format(Username))
                TransmitClientsMessages(clientsocket, Username, Message)
                i+=1
        except Exception as x:
            screen.insert(i,'%s is now disconnected' % Username)
            i+=1
            break

# Using Nickname, client's IP adress and his message, the server transmit or
# broadcast the user's messages to all connected clients in the clients list
def TransmitClientsMessages(clientsocket, Username, Message):
    for client in Clients:
        # Server checks the sockets so it doesn't broadcast the message back
        # to the user who wrote it. Then, it broadcasts the messages to all other connected clients
        if client[1] != clientsocket:
            client[1].send(Username.encode('ascii'))
            client[1].send(Message.encode('ascii'))

#=============================================================================================

# TCP Connection:

# Creating a socket
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# Establishing a connection
HOST = socket.gethostname() # The Localhost IP Adress
PORT = 4444
serversocket.bind( (HOST, PORT) )
screen.insert(1,'Chat server started on port : ' + str(PORT))

# The server is waiting any clients trying to connect
# Whenever a client is found, it creates a thread for him
serversocket.listen(1)
ConnectionThread = threading.Thread( target = Connection )
ConnectionThread.start()

Interface2.mainloop()


#=============================================================================================
#=============================================================================================
