from client0 import Client
from seq1 import Seq
import termcolor
PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "localhost"
PORT = 8080
c = Client(IP, PORT)
print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")
s = Seq()
s.seq_read_fasta("FRAT1")
s1 = Seq()
s1.seq_read_fasta("U5")
s2 = Seq()
s2.seq_read_fasta("")
#hacer lo de ficheros en ficheros
print("To server: ")
termcolor.cprint()
response = c.talk("Testing!!!")
print(f"Response: {response}")