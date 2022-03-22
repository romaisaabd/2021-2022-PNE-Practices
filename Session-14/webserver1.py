import http.server
import socketserver

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
# -- TCPserver is a protocol below HTTP

# -- Use the http.server Handler
Handler = http.server.SimpleHTTPRequestHandler
# -- SimpleHTTPRequestHandler is a class inside the http.server
# -- "" mean any interface in my computer
# -- un Handler es un "manejador", algo que es capaz de "recibir" un evento, un mensaje, etc y actuar en función al mismo.
# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped!")
        httpd.server_close()