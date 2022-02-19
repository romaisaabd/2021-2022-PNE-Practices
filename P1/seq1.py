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
        if self.strbases == "NULL" and self.strbases == "ERROR":
            self.strbases = ""
        return len(self.strbases)

    def count_base(self,strbases):
        """Calculate the bases of the sequence"""
        d = {"A": 0, "C": 0, "G": 0, "T": 0, }
        if self.strbases != "":
            for b in strbases:
                d[b] += 1
            return d
        else:
            print(d)


