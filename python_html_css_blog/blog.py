import http.server
import socketserver
import os

class blog_server(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == '/':
            self.path = 'blog.html'
        elif self.path == "/home.html":
            file_list = os.listdir("./blog-posts")
            open("home.html","w").write("<!DOCTYPE html>\n<html>\n<head>\n<title>TEST FILE</title>\n</head>\n<body>\n<p>The list of files in \\blog-posts folder are:</p>\n<ul>\n")
            for i in range(len(file_list)):
                open("home.html", "a").write("<li><a href=\"{filename" + str(i) +"}\">{filename" + str(i) + "}</li>\n")
            open("home.html","a").write("</ul>\n</body>\n</html>\n")
            newfile = open("home.html").read().format(filename0 = file_list[0], filename1 = file_list[1], filename2 = file_list[2])
            open("home.html", "w").write(newfile)
            # filename = "filename"
            # for i in range(len(file_list)):
            #     filename = filename + str(i)
            #     print(filename)
            #     open("home.html").read().format(filename = file_list[i])
            self.path = "home.html"
            
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    

handler_object = blog_server

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)


my_server.serve_forever()