from pathlib import Path


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases ="NULL"):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        self.strbases = strbases
        if self.strbases == "NULL":
            print("NULL Seq Created")
        elif not self.valid_sequence():
            self.strbases = "ERROR"
            print("INVALID Seq!")
        else:
            print("New sequence created!")

    @staticmethod
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def valid_sequence(self):
        valid = True
        i = 0
        while i< len(self.strbases) and valid:
            c = self.strbases[i]
            if c!= "A" and c!= "C" and c!= "G" and c!= "T":
                valid =  False
            i += 1
        return valid

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            result = 0
        else:
            result = len(self.strbases)
        return result

    def count_base(self,list_bases):
        """Calculate the number of bases using lists"""
        count = 0
        if self.strbases == "ERROR" or self.strbases == "NULL":
            count = 0
        else:
            for s in self.strbases:
                if s == list_bases:
                    count += 1
        return count

    def count(self,strbases):
        """Calculate the bases of the sequence using dictionaries"""
        d = {"A": 0, "C": 0, "G": 0, "T": 0, }
        if self.strbases != "ERROR" and self.strbases != "NULL":
            for b in strbases:
                d[b] += 1
            result = d
        else:
            result = d
        return result

    def reverse(self):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            result = self.strbases
        else:
            result = ''.join(reversed(self.strbases))
        return result

    def complement(self,strbases):
        if self.strbases != "ERROR" or self.strbases != "NULL":
            complementary_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
            for b in strbases:
                complementary_bases[b] == a
            result=




        else:
            result = self.strbases
        return result

    def seq_complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            complement_dict = {"A": "C", "C": "A", "T": "G", "G": "T"}
            new_seq = ""

            for e in self.strbases:
                for b in complement_dict:
                    if e == b:
                        new_seq += complement_dict[b]

            return new_seq

    def read_fasta(self,filename):
        seq = Path(filename).read_text()
        new_seq = seq.find("\n")
        seq = seq[new_seq:].replace("\n", "")
        self.strbases = seq
        return seq
    
















