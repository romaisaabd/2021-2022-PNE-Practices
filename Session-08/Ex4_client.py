import socket

import colorama

# SERVER IP, PORT
PORT = 8000
IP = "localhost"
while True:
    msg = input("Introduce your message in the chat: ")
    # First, create the socket
    # We will always use this parameters: AF_INET y SOCK_STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT)) #esta es una tupla si ponemos solo con un paréntesis -->> nos pondría takes exactly one argument (2 given)

    # Send data. No strings can be send, only bytes
    # It necesary to encode the string into bytes
    s.send(str.encode(msg))

    # Receive data from the server
    msg = s.recv(2048)
    print("MESSAGE FROM THE SERVER:\n")
    colorama.init()
    #termcolor.cprint(msg.decode("utf-8"), "green")
    print(colorama.Fore.BLUE + msg.decode("utf-8"))

    # Closing the socket
    s.close()
