from http.server import HTTPServer, BaseHTTPRequestHandler

class server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "for_response.html"
            html_file = open(self.path).read()
            self.send_response(200)
        
        self.end_headers()
        self.wfile.write(bytes(html_file, 'utf-8'))

PORT = 8000
page = HTTPServer(('localhost', PORT), server)
page.serve_forever()