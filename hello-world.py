#!/usr/bin/python3
import subprocess
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

# This class will handle any incoming request from the browser
class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send the HTML message
        self.wfile.write(b"Hello World !!")
       # self.wfile.write(bytes("WELCOME_MSG : " + os.getenv('WELCOME_MSG', 'undef') + "\n", "utf-8"))
       # self.wfile.write(bytes("Hostname is : " + subprocess.check_output("uname -n", shell=True).decode("utf-8"), "utf-8"))
       # self.wfile.write(bytes("Process ID  : " + str(os.getpid()), "utf-8"))
        return


try:
    # Create a web server and define the handler to manage incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print("Started httpserver on port", PORT_NUMBER)

    # Wait forever for incoming HTTP requests
    server.serve_forever()

except KeyboardInterrupt:
    print("^C received, shutting down the web server")
    server.socket.close()
