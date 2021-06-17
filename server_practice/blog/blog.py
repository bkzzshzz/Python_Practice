import http.server
import socketserver

class blog_server(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'blog.html'
        elif self.path in ['/home', '/index.html','/my_bio.html','/my_bio']:
            self.path = 'my_bio.html'
        elif self.path in ['/contact','/contact-me','/contact.html', '/my_contact', '/my_contact.html']:
            self.path = 'my_contact.html'
        elif self.path in ['/hobby','/hobbies','/hobby.html','/hobbies.html']:
            self.path = 'hobbies.html'
        elif self.path in ['/gallery','/gallery.html']:
            self.path = 'gallery.html'
        else:
            self.path = '404.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler_object = blog_server

PORT = 8003
my_server = socketserver.TCPServer(("", PORT), handler_object)


my_server.serve_forever()