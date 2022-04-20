from urllib.parse import parse_qs

def read_html_file(filename):
    contents = Path(HTML_FOLDER)

HTML_FOLDER = "./HTML/"
LIST_SEQUENCES = ["CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
             "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
             "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
             "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
             "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"]

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        url_path = u.urlparse(self.path)
        path = url_path.path
        argument = parse_qs(url_path.query)
        print("The old  path is ", self.path)
        print("The new path is ", url_path.path) #este no tiene el signo de interrogación
        print(argument)
        # Open the form1.html file
        # Read the index from the file

        if path == "/":
            contents = read_html_file("index.html").render(context = {"n_sequences": len(LIST_SEQUENCES)})
        if path == "get/":
            n_sequence = int(argument["n_sequence"][0]) #no necesitmos exceptions porque estamos obligando que sea,,,,
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(Path[1:] + ".html").render()
        elif self.path == "/favicon.ico":
            contents =Path("HTML/form-1.html").read_text()
        elif path == "/ping?":
           contents =
        else:
            try:
                filename = self.path
                f_filename = filename.replace("/","").replace("?","")
                contents = Path("HTML/" + f_filename + ".html").read_text()
            except IndexError:
                contents = Path("HTML/Error.html").read_text()
            except FileNotFoundError:
                contents = Path("HTML/Error.html").read_text()