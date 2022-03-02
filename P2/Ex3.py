from client0 import Client
PRACTICE = 2
EXERCISE = 3
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
# -- Parameters of the server to talk to
IP = "localhost"
PORT = 8080
c = Client(IP, PORT)
print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
