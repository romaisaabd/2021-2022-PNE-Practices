class Seq:
    """A class for representing sequences"""

    def __init__(self,strbases):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        self.strbases = strbases
        if not self.valid_sequence():
            self.strbases = "ERROR"
            print("ERROR!!")
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
        return len(self.strbases)