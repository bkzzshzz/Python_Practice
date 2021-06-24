import http.server
import socketserver
import os

PORT = 8001
class blog_server(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == '/':
            self.path = '/home.html'

        if self.path == "/home.html":
            file_list = os.listdir("./blog-posts")
            template_string = open("home.template.html", "r").read()
            
            
            link_for_single_file = '''
            <li><a href="blog-posts/{file_name}">{file_title}</a></li>
            '''
            list_of_links = '''
            '''
            for name_of_file in file_list:
                # Following code extracts title form <title> -------- </title> section of each file
                file_handle = open("./blog-posts/" + name_of_file)
                file_content_str = file_handle.read()
                starting_pos = file_content_str.find('<title>') + len('<title>')
                ending_pos = file_content_str.find('</title>')
                title_from_file = file_content_str[starting_pos:ending_pos]
                list_of_links = list_of_links + link_for_single_file.format(file_name = name_of_file, file_title = title_from_file)
            
            new_file = template_string.format(variable = list_of_links)
            open("home.html", "w").write(new_file) 
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    print (f"BLOG SERVER: I am running on http://localhost:{PORT}")
    my_server = socketserver.TCPServer(("", PORT), blog_server)
    my_server.serve_forever()
