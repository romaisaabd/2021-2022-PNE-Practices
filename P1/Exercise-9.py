from seq1 import Seq
print("-----| Practice 1, Exercise 9 |------")
# -- Create a Null sequence
s = Seq()
# -- Initialize the null seq with the given file in fasta format
s.read_fasta("U5")
print(s)
print(s.len())
