import socket

from seq1 import Seq

import termcolor


def count_bases(arg):
    d = {"A": 0, "C": 0, "G": 0, "T": 0, }
    for b in str(arg):
        d[b] += 1
    total = sum(d.values())
    for k, v in d.items():
        d[k] = [v, (v * 100) / total]
    return d


def convert_msg(base_count):
    message = ""
    for k, v in base_count.items():
        message += k + ":" + str(v[0]) + "(" + str(round(v[1], 1)) + "%" + ")" + "\n"
    return message


def info_operation():
    base_count = count_bases(arg)
    response = "Sequence:" + arg + "\n"
    response += "Total length:" + str(len(arg)) + "\n"
    response += convert_msg(base_count)
    return response


sequences = ["CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
             "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
             "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
             "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
             "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"]

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = "127.0.0.1"
PORT = 8082

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
                response = sequences[int(arg)] + "\n"
            except ValueError:
                response = "The argument must be an integer number."
            except IndexError:
                response = "The argument must be a number between 0 and 4 both included\n"

        elif cmd == "REV":
            response = arg[::-1] + "\n"
            print(response)

        elif cmd == "INFO":
            try:
                response = info_operation(arg)
                print(response)
            except ZeroDivisionError:
                response = "Pycharm cannot preform this operation (we cannot divide by 0) \n"

        elif cmd == "COMP":
            sequence = Seq(arg)
            response = sequence.complement() + "\n"
            print(response)

        elif cmd == "GENE":
            try:
                sequence = Seq()
                response = sequence.read_fasta(str(arg)) + "\n"
                print(response)
            except FileNotFoundError:
                response = "The file does not exist.\n"


        else:
            response = "This command is not available in the server.\n"

        cs.send(response.encode())
        cs.close()
