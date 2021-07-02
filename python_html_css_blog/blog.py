import http.server
import socketserver
import os

PORT = 8001
rendered_folder = 'rendered_html/'
template_folder = 'template_html/'

class blog_server(http.server.SimpleHTTPRequestHandler):
   
    def do_GET(self):
        navbar = open("partials/header.template.html").read()
        body_script = open("partials/scripts.template.html").read()
        print(f'BLOG SERVER: The requested path is: {self.path}')
        file_list = os.listdir("./blog-posts")
        template_string = open(template_folder + "home.template.html", "r").read()
        link_for_single_file = '''
        <li><a href="blog-posts/{file_name}">{file_title}</a></li>
        '''
        list_of_links = '''
        '''
        get_file = False

        for name_of_file in file_list:
            # Following code extracts title form <title> -------- </title> section of each file
            file_handle = open("./blog-posts/" + name_of_file)
            file_content_str = file_handle.read()
            temp_file = file_content_str
            temp_file = temp_file.lower()
            starting_pos = temp_file.find('<title>') + len('<title>')
            ending_pos = temp_file.find('</title>')
            title_from_file = file_content_str[starting_pos:ending_pos]
            list_of_links = list_of_links + link_for_single_file.format(file_name = name_of_file, file_title = title_from_file)

        if self.path == '/home.html' or self.path == "/":
            new_file = template_string.format(variable = list_of_links, header = navbar, scripts = body_script)
            open(rendered_folder + "home.html", "w").write(new_file)
            self.path = rendered_folder + "home.html"
            get_file = True


        elif self.path == "/all-posts.html":
            template_string = open(template_folder + "all-posts.template.html").read().format(variable = list_of_links, header = navbar, scripts = body_script)
            open(rendered_folder + "all-posts.html","w").write(template_string)
            self.path = rendered_folder + "all-posts.html"
            get_file = True

        if self.path[0:12] == '/blog-posts/':
            requested_post_filename = self.path[12:]
            try:
                template_string = open ('blog-posts/' + requested_post_filename).read().format(header = navbar, scripts = body_script)
                open(rendered_folder + requested_post_filename, "w").write(template_string)
                self.path = rendered_folder + requested_post_filename
                get_file = True
            except Exception as e:
                print ('BLOG SERVER: caught an exception while trying to access that file ')
                print (f'BLOG SERVER: {e}')
                self.path = "404.html"

        

        pages_in_blog = os.listdir("./rendered_html")
        
        if self.path[1:] in pages_in_blog:
            template_string = open(template_folder + self.path[1:-5] + ".template.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + self.path[1:], "w").write(template_string)
            self.path = rendered_folder + self.path[1:]
            get_file = True
        
        if self.path.endswith('.jpg'):
            get_file = True

        if not get_file:
            self.path = "404.html"
        print(f'MY SERVER: The redirected path is: {self.path}')

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    print (f"BLOG SERVER: I am running on http://localhost:{PORT}")
    my_server = socketserver.TCPServer(("", PORT), blog_server)
    my_server.serve_forever()
