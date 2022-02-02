def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0,}
    for b in seq:
        d[b] += 1 #probarlo con lo de if y elif
    return d




dna_seq = input("Introduce a sequence: ")
print("Total length:", len(dna_seq))
#print(d)
#print(count_bases(dna_seq))#probar con dna_seq en la función
for k,v in count_bases(dna_seq).items():
    print(k+":", v)