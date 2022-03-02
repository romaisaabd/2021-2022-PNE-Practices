from client0 import Client
PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "localhost"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")