import socket

from seq1 import Seq

import termcolor

sequences = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
             "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
             "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
             "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
             "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]

def info_operation():
    seq = Seq()
    response = "Sequence:" + split_list[1] + "\n"
    response += "Total length:" + str(seq.len()) + "\n"
    dictionary_bases = seq.percentages()
    response += ""
    for k, v in dictionary_bases.items():
        response += k + ":" + str(v[0]) + "(" + str(round(v[1], 1)) + "%" + ")" + "\n"
    return response


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "0.0.0.0"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

while True:
    print("Waiting for Clients to connect...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().replace("\n", "").strip().upper()
        split_list = msg.split(" ")

        cmd = split_list[0]

        if cmd != "PING":
            arg = split_list[1]
        termcolor.cprint(f"{cmd}", "green")

        if cmd == "PING":
            response = "OK\n"

        elif cmd == "GET":
            arg = split_list[1]
            try:
                response = sequences[int(arg)]
            except IndexError and ValueError:
                response = "The number must be and integer between 0 and 4 both included\n"

        elif cmd == "REV":
            #I did not handle the error that the sequence must be valid using ACGT and not other bases that does not exist
            response = arg[::-1]
            print(response)

        elif cmd == "INFO":
            try:
                response = info_operation()
                print(response)
            except ZeroDivisionError:
                response = "Can not perform this operation\n"







        cs.send(response.encode())
        cs.close()
