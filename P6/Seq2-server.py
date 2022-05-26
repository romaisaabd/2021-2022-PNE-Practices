import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
import urllib.parse as u
"""
def count_bases(arg):
    d = {"A": 0, "C": 0, "G": 0, "T": 0, }
    for b in str(arg):
        d[b] += 1
    total = sum(d.values())
    for k, v in d.items():
        d[k] = [v, (v * 100) / total]
    return d

def read_html_file(filename):
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
    return response"""
# Define the Server's port
PORT = 8080
HTML_FOLDER ="./HTML/"
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        url_path = u.urlparse(self.path)
        path = url_path.path
        print("The old  path is ", self.path)
        print("The new path is ", url_path.path) #este no tiene el signo de interrogación
        # Open the form1.html file
        # Read the index from the file
        route = self.requestline.split(" ")[1]
        print(self.path)
        if len(self.requestline) > 0:
            if self.path == "/":
                contents = Path("HTML/form-1.html").read_text()
            elif self.path == "/favicon.ico":
                contents =Path("HTML/form-1.html").read_text()
            elif path == "/ping?":
               #contents = Path("HTML/ping.html").read_text()
    """     else:
                try:
                    filename = self.path
                    f_filename = filename.replace("/","").replace("?","")
                    contents = Path("HTML/" + f_filename + ".html").read_text()
                except IndexError:
                    contents = Path("HTML/Error.html").read_text()
                except FileNotFoundError:
                    contents = Path("HTML/Error.html").read_text()"""



        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()