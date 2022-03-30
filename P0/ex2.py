import seq0
filename = seq0.valid_filename()
sequence = seq0.seq_read_fasta(filename)

print("DNA filename: ", filename)
print("The first 20  bases:", sequence[0:20])

