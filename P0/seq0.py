def seq_ping():
    print("Ok")

#EXERCISE 1
def valid_filename(FOLDER):
    exit = False
    while not exit:
        filename = input("DNA file:")
        try:
            f= open(FOLDER + filename + ".txt","r")
            exit = True
            return filename
        except FileNotFoundError:
            print("This file has not been found")

#EXERCISE 2
def seq_read_fasta(filename,FOLDER):
    seq = open(FOLDER + filename + ".txt","r").read()
    new_seq = seq.find("\n")
    seq = seq[new_seq:].replace("\n","")
    return seq

#EXERCISE 3
def seq_len(seq):
    list_genes = []
    for i in seq:
        list_genes.append(len(seq_read_fasta(i)))
    return list_genes

#EXERCISE 4
def seq_count_base(seq,base):
    bases_list = ["U5", "ADA", "FRAT1", "FXN"]


















