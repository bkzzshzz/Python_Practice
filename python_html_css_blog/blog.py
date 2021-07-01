import http.server
import socketserver
import os

PORT = 8000
rendered_folder = 'rendered_html/'
template_folder = 'template_html/'

class blog_server(http.server.SimpleHTTPRequestHandler):
   
    def do_GET(self):

        navbar = open("partials/header.template.html").read()
        body_script = open("partials/scripts.template.html").read()
        print(f'MY SERVER: The requested path is: {self.path}')

              
        
        if self.path == '/':
            self.path = rendered_folder + 'home.html'

        if self.path == "/home.html" or self.path == "/":
            file_list = os.listdir("./blog-posts")
            template_string = open(template_folder + "home.template.html", "r").read()
            
            
            link_for_single_file = '''
            <li><a href="blog-posts/{file_name}">{file_title}</a></li>
            '''
            list_of_links = '''
            '''
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
            
            new_file = template_string.format(variable = list_of_links, header = navbar, scripts = body_script)
            open(rendered_folder + "home.html", "w").write(new_file)
            self.path = rendered_folder + "home.html"
        elif self.path == "/book_reviews.html":
            template_string = open(template_folder + "book_reviews.template.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + "book_reviews.html", "w").write(template_string)
            self.path = rendered_folder + "book_reviews.html"
        elif self.path == "/gallery.html":
            template_string = open(template_folder + "gallery.template.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + "gallery.html", "w").write(template_string)
            self.path = rendered_folder + "gallery.html"
        elif self.path == "/programming_journey.html":
            template_string = open(template_folder + "programming_journey.template.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + "programming_journey.html", "w").write(template_string)
            self.path = rendered_folder + "programming_journey.html"
        elif self.path == "/poems.html":
            template_string = open(template_folder + "poems.template.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + "poems.html", "w").write(template_string)
            self.path = rendered_folder + "poems.html"
        elif self.path == "/my_cv.html":
            template_string = open(template_folder + "my_cv.template.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + "my_cv.html", "w").write(template_string)
            self.path = rendered_folder + "my_cv.html"
        elif self.path == "/blog-posts/first-post.html":
            template_string = open("blog-posts/first-post.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + "first-post.html", "w").write(template_string)
            self.path = rendered_folder + "first-post.html"
        elif self.path == "/blog-posts/my-childhood.html":
            template_string = open("blog-posts/my-childhood.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + "my-childhood.html", "w").write(template_string)
            self.path = rendered_folder + "my-childhood.html"
        elif self.path == "/blog-posts/who-is-syd-barret.html":
            template_string = open("blog-posts/who-is-syd-barret.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + "who-is-syd-barret.html", "w").write(template_string)
            self.path = rendered_folder + "who-is-syd-barret.html"
        else:
            self.path = "404.html"
        print(f'MY SERVER: The redirected path is: {self.path}')

        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    print (f"BLOG SERVER: I am running on http://localhost:{PORT}")
    my_server = socketserver.TCPServer(("", PORT), blog_server)
    my_server.serve_forever()
