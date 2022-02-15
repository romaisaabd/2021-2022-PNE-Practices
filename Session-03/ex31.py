# That's the DNA_count_file

# Description: Write a program that opens the dna.txt file and calculates the total number of bases,
# and the number of the different bases

def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0,}
    for b in seq:
        d[b] += 1
    return d



def print_info():
    with open("dna.txt", "r") as f:
        sequences = f.readlines()
        for seq in sequences:
            new_seq = seq.replace("\n", "")
            for k, v in count_bases(new_seq).items():
                print(k + ":", v)