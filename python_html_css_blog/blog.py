import http.server
import socketserver

class blog_server(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("The current page")
        print(self.path)
        if self.path == '/':
            self.path = 'blog.html'
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    

handler_object = blog_server

PORT = 8007
my_server = socketserver.TCPServer(("", PORT), handler_object)


my_server.serve_forever()