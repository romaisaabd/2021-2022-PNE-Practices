from seq1 import Seq
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]


def print_seqs(seq_list):
    for i in range(0, len(seq_list)):
        print("Sequence 0: ", "(Length: ", len(seq_list[]), ")", )