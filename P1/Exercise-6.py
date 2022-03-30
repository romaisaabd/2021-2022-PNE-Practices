from seq1 import Seq
print("-----| Practice 1, Exercise 6 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 0:(Length: {s1.len()})", s1, f"\nBases:{s1.count()})")
print(f"Sequence 1: (Length: {s2.len()})", s2, f"\nBases:{s2.count()})")
print(f"Sequence 2: (Length: {s3.len()})", s3, f"\nBases:{s3.count()})")