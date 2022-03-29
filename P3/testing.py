
elif cmd == "INFO":
try:
    response = info_operation()
    print(response)
except ZeroDivisionError:
    response = "Can not perform this operation\n"

elif cmd == "COMP":
response = seq.complement() + "\n"
print(response)

elif cmd == "GENE":
try:
    s1 = Seq()
    response = s1.read_fasta(str(arg))
    print(response)
except FileNotFoundError:
    response = "The file was not found\n"

else:
    response = "This command is not available in the server.\n"