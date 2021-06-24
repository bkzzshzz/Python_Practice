import http.server
import socketserver
import os

class blog_server(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == '/':
            self.path = 'blog.html'
        elif self.path == "/home.html":
            file_list = os.listdir("./blog-posts")
            template = open("home.template.html", "r").read()
            new_file = open("home.html","w").write(template)
            
            
            for i in range(len(file_list)):
                print(i)
                link_list = "<li><a href=\"{filename" + str(i) +"}\">{filename" + str(i) + "}</li>\n{variable}\n"
                print(link_list)
                new_file = open("home.html").read().format(variable = link_list)
                print(new_file)
                open("home.html", "w").write(new_file)
            
            newfile = open("home.html").read().format(filename0 = file_list[0], filename1 = file_list[1], filename2 = file_list[2], variable = "")
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