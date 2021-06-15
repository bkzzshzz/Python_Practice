from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
    prompt = ""
    def do_GET(self):

        if self.path == '/':
            prompt = "Hello World!"
            self.send_response(200)
        else:
            prompt = "File not found"
            self.send_response(404)
        self.end_headers() #required by BaseHTTPRequestHandler
        self.wfile.write(bytes(prompt, 'utf-8')) #convert output to bytes and utf-8 is an encoding method


httpd = HTTPServer(('localhost', 8000), Serv) #Background work, 8000 is the port, localhost is the server
httpd.serve_forever()
