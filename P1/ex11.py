from seq1 import Seq
#s1 = Seq("ACCTGC")
#s2 = Seq("Hello? Am I a valid sequence?")
#print(f"Sequence 1: {s1}")
#print(f"Sequence 2: {s2}")

#ha eliminado lo que habbia debajo de strbases

str_list = ["ACCTGC","Hello? Am I a valid sequence?"]
sequence_list = []
for st in str_list:
    if Seq.valid_sequence2(st):
        sequence_list.append(Seq(st))
    else:
        sequence_list.append(Seq("ERROR"))
for i in range (0,len(sequence_list)):
    print("Sequence",str(i) + ":",sequence_list[i])