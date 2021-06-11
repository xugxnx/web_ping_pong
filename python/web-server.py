from http.server import HTTPServer, BaseHTTPRequestHandler
import re

portnum = 8080

class BaseServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if re.search("/ping", self.requestline):
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write("pong".encode())

server = HTTPServer(("", portnum),BaseServer)
server.serve_forever()