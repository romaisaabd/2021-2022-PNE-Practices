from client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)


print("* Testing PING...")
msg = c.talk("PING")
print(msg)

print("* Testing GET 0...")
msg = c.talk("GET 0")
print(msg)

print("* Testing GET 1...")
msg = c.talk("GET 1")
print(msg)

print("* Testing GET 2...")
msg = c.talk("GET 2")
print(msg)

print("* Testing GET 3...")
msg = c.talk("GET 3")
print(msg)

print("* Testing GET 4...")
msg = c.talk("GET 4")
print(msg)

print("\n* Testing INFO...")
msg = c.talk("INFO ACTAG")
print(msg)

print("* Testing COMP...")
msg = c.talk("COMP ACTAG")
print(msg)

print("* Testing REV...")
msg = c.talk("REV ACTAG ")
print(msg)

print("* Testing GENE...")
msg = c.talk("GENE U5")
print(msg)