from client0 import Client
from seq1 import Seq

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")

s1 = Seq()
sequence = s1.read_fasta("FRAT1")
print("Gene FRAT1:", s1)
c.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")

i = 0
x = 10
count = 0
while i < 50:
    splt_seq = sequence[i:x]
    i += 10
    x += + 10
    count += 1
    print(f"Fragment {count}: {splt_seq}")
    c.talk(f"Fragment {count}: {splt_seq}")