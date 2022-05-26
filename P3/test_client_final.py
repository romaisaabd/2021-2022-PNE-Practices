from client0 import Client
IP = "localhost"
PORT = 6791
sequence = "ACGTGCGA"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

c = Client(IP, PORT)

print("* Testing PING...")
msg = c.talk("PING")
print(msg)

for n in range(5):
    print(f"* Testing GET {n}...")
    msg = c.talk(f"GET {n}")
    print(msg)

print(f"* Testing INFO {sequence}...")
msg = c.talk(f"INFO {sequence}")
print(msg)

print(f"* Testing COMP {sequence}...")
msg = c.talk(f"COMP {sequence}")
print(msg)


print(f"* Testing REV {sequence}...")
msg = c.talk(f"REV {sequence}")
print(msg)

for g in genes:
    print(f"* Testing GET {g}...")
    msg = c.talk(f"GENE {g}")
    print(msg)

for n in range(6):
    print(f"* Testing TUP {n}...")
    msg = c.talk(f"TUP {n}")
    print(msg)
