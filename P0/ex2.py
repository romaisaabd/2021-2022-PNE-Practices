import seq0
FOLDER = "./sequences/"
sequence = seq0.seq_read_fasta((seq0.valid_filename(FOLDER)), FOLDER)
print("The first 20  bases:", sequence[0:20])

