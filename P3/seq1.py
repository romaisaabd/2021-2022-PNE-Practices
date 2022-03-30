class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases ="NULL"):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        self.strbases = strbases
        if strbases == "NULL":
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

    def count(self):
        """Calculate the bases of the sequence using dictionaries"""
        d = {"A": 0, "C": 0, "G": 0, "T": 0, }
        if self.strbases != "ERROR" and self.strbases != "NULL":
            for b in self.strbases:
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

    def complement(self):
        if self.strbases != "ERROR" or self.strbases != "NULL":
            com_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
            com_string= ""
            for b in self.strbases:
                for i in com_bases:
                    if b == i:
                        com_string += com_bases[i]
            return com_string
        else:
            return self.strbases

    def read_fasta(self, filename):
        seq = open("./sequences/" + filename + ".txt", "r").read()
        seq = seq[seq.find("\n"):].replace("\n", "")
        self.strbases = seq
        return seq

    def percent_bases(self):
        dictionary = self.count()
        total = len(self.strbases)
        for k in dictionary:
            dictionary[k] = (dictionary[k] / total * 100)
        return dictionary

    def info_operation(self,arg):
        d = {"A": 0, "C": 0, "G": 0, "T": 0, "A%": 0, "C%": 0, "G%": 0, "T%": 0}
        for b in arg:
            d[b] += 1
            d[b + "%"] = round((d[b] / len(arg) * 100), 2)
        response = f"Sequence: {arg}\nTotal length: {len(arg)}\n A: {d['A']} ({d['A%']} %)\n C: {d['C']} ({d['C%']} %)\n G: {d['G']} ({d['G%']} %)\n T: {d['T']} ({d['T%']} %)\n"
        return response