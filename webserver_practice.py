from http.server import HTTPServer, BaseHTTPRequestHandler #http.sever is a package
#HTTPServer and BaseHTTPRequestHandler are built in classes

class Serv(BaseHTTPRequestHandler): #inheriting methods from BaseHTTPRequestHandler

    def do_GET(self): # Cant rename #Get request method built-in BaseHTTPRequestHandler

        if self.path == '/':
            self.path = '/my_html.html'
            self.path = '/my_html1.html'
            self.path = '/my_html2.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers() #required by BaseHTTPRequestHandler
        self.wfile.write(bytes(file_to_open, 'utf-8')) #convert output to bytes and utf-8 is an encoding method


httpd = HTTPServer(('localhost', 8000), Serv) #Background work, 8000 is the port, localhost is the server
httpd.serve_forever()
