import socket
import termcolor
import colorama

# SERVER IP, PORT
PORT = 8000
#IP = "212.128.253.64"--> IP the la clase de David
#IP = "10.3.46.157"--> IP of Rafa's teacher
#IP = "10.3.55.58" #en el server tenia localhost y da error
#IP = "localhost" --> que es el mismo que poner"127.0.0.1"
IP = "" #si lo ponemos en el server da igual lo que pongamos en el ip del cliente

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = s.recv(2048)
print("MESSAGE FROM THE SERVER:\n")
colorama.init()
#termcolor.cprint(msg.decode("utf-8"), "green")
print(colorama.Fore.BLUE + msg.decode("utf-8"))

# Closing the socket
s.close()