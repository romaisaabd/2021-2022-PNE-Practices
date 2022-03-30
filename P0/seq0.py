def seq_ping():
    print("Ok")

def valid_filename():
    exit = False
    while not exit:
        filename = input("DNA file:")
        try:
            f= open("./sequences/" + filename + ".txt","r")
            exit = True
            return filename
        except FileNotFoundError:
            print("This file has not been found")

def seq_read_fasta(filename,FOLDER):
    seq = open("./sequences/" + filename + ".txt","r").read()
    new_seq = seq.find("\n")
    seq = seq[new_seq:].replace("\n","")
    return seq

def seq_len(seq):
    list_genes = []
    for i in seq:
        list_genes.append(len(seq_read_fasta(i)))
    return list_genes

def seq_count_base(seq):
    #seq = open("./sequences/" + seq + ".txt", "r").read()
    #seq = seq[seq.find("\n"):].replace("\n", "")
    data_list = []
    for i in seq:
        data_list.append(seq_read_fasta(i))
    return seq

















