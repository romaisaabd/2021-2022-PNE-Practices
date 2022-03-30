from seq1 import Seq
print("-----| Practice 1, Exercise 9 |------")
try:
      s1 = Seq()
      s1.read_fasta("U5")
      print(f"Sequence: (Length: {s1.len()}"")", s1,
            "\n\tBases:",s1.count(),
            "\n\tRev:",s1.reverse(),
            "\n\tComp:",s1.complement())

except FileNotFoundError:
      print("The file has not been found.")

