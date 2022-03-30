from seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

seq_list = ["U5","ADA","FRAT1","FXN","RNU6_269P"]

try:
    for s in seq_list:
        s1 = Seq()
        s1.read_fasta(s)
        print("Gene", s, ": Most frequent Base:",max(s1.count(), key = s1.count().get))

except FileNotFoundError:
    print("This file does not exist.")