from seq1 import Seq
print("-----| Practice 1, Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
list_bases = ["A","C","G","T"]
print(f"Sequence 1:(Length: {s1.len()})", s1)
for l in list_bases:
    print(l + ":", s1.count_base(l), end=",")
print(f"\nSequence 2: (Length: {s2.len()})", s2)
for l in list_bases:
    print(l + ":", s2.count_base(l), end=",")
print(f"\nSequence 3: (Length: {s3.len()})", s3)
for l in list_bases:
    print(l + ":", s3.count_base(l), end=",")