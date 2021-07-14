import http.server
import socketserver
import os
import random
import csv

def valid_name(name):
    result = ""
    for each_letter in name:
        if each_letter == "+" or each_letter.isalpha():
            result =  True
        else:    
            result = False
            break
    return result


def proper_name(name):
    words_in_name = name.split("+")
    temp_name = []
    for each_word in words_in_name:
        if each_word != "":
            temp_name.append(each_word)
    words_in_name = temp_name.copy()
    temp_name = []
    for each_word in words_in_name:
        temp_word = each_word.lower()
        temp_word = temp_word[0].upper() + temp_word[1:]
        temp_name.append(temp_word)
    words_in_name = temp_name.copy()
    return " ".join(words_in_name)


def email_okay(email, variable):
    if email not in variable:
        return True


def password_match(password, re_password):
    if password == re_password:
        return True
    else:
        return False


PORT = random.randrange(8000, 8005)
rendered_folder = 'rendered-html/'
template_folder = 'template-html/'

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
        
        elif self.path == "/signup.html":
            template_string = open(template_folder + "views/signup.template.html").read().format(message = "")
            open(rendered_folder + "signup.html", "w").write(template_string)
            self.path = rendered_folder + "signup.html"
            get_file = True

        elif self.path == "/login.html":
            template_string = open(template_folder + "views/login.template.html").read().format(message = "")
            open(rendered_folder + "login.html", "w").write(template_string)
            self.path = rendered_folder + "login.html"
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

        template_files = os.listdir("./template-html")
        pages_in_blog = []

        for each_page_in_blog in template_files:
            pages_in_blog.append(each_page_in_blog[:-14] + ".html")
        
        if self.path[1:] in pages_in_blog:
            template_string = open(template_folder + self.path[1:-5] + ".template.html").read().format(header = navbar, scripts = body_script)
            open(rendered_folder + self.path[1:], "w").write(template_string)
            self.path = rendered_folder + self.path[1:]
            get_file = True
        
        valid_extensions = ['.jpg', '.css', '.js', '.eot', '.tff', '.woff', '.woff2', '.ico']

        for extension in valid_extensions:
            if self.path.endswith(extension):
                get_file = True
                break
        #to do social media icons not loading

        if not get_file:
            self.path = "404.html"
            self.send_response(404)
        print(f'MY SERVER: The redirected path is: {self.path}')

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):

        if self.path == "/signup":
            content_length = int(self.headers['Content-Length'])
            post_data_bytes = self.rfile.read(content_length)
            post_data_str = post_data_bytes.decode("UTF-8")
            list_of_post_data = post_data_str.split('&')
            post_data_dict = {}

            for item in list_of_post_data:
                title, value = item.split('=')
                post_data_dict[title] = value

            temp_name = str(post_data_dict['name'])
            email = str(post_data_dict['email'])
            password = str(post_data_dict['pass'])
            re_password = str(post_data_dict['re_pass'])
            try:
                variable = open("user-info.txt").read()
            except:
                variable = open("user-info.txt", "w").write("name,email,password\n")
            
            
            if not valid_name(temp_name):
                template_string = open(template_folder + "views/signup.template.html").read().format(message = "Invalid name")
                open(rendered_folder + "signup.html", "w").write(template_string)
                self.path = rendered_folder + "signup.html"

            elif not email_okay(email, variable):
                template_string = open(template_folder + "views/signup.template.html").read().format(message = "Email already exists")
                open(rendered_folder + "signup.html", "w").write(template_string)
                self.path = rendered_folder + "signup.html"

            elif password == None or re_password == None:
                template_string = open(template_folder + "views/signup.template.html").read().format(message = "Password cannot be blank")
                open(rendered_folder + "signup.html", "w").write(template_string)
                self.path = rendered_folder + "signup.html"
            
            elif len(password) < 6:
                template_string = open(template_folder + "views/signup.template.html").read().format(message = "Password should be longer than 6 characters")
                open(rendered_folder + "signup.html", "w").write(template_string)
                self.path = rendered_folder + "signup.html"

            elif not password_match(password, re_password):
                template_string = open(template_folder + "views/signup.template.html").read().format(message = "Passwords do not match")
                open(rendered_folder + "signup.html", "w").write(template_string)
                self.path = rendered_folder + "signup.html"
            
            else:
                name = proper_name(temp_name)
                try:
                    str(post_data_dict['agree-term'])
                    template_string = open(template_folder + "views/signup.template.html").read().format(message = "Success!")
                    open(rendered_folder + "signup.html", "w").write(template_string)
                    open("user-info.txt", "a").write(name + ", " + email + ", " + password + "\n")
                    self.path = rendered_folder + "signup.html"
                except:
                    template_string = open(template_folder + "views/signup.template.html").read().format(message = "Checkbox not checked")
                    open(rendered_folder + "signup.html", "w").write(template_string)
                    self.path = rendered_folder + "signup.html"
            
        if self.path == "/login":
            content_length = int(self.headers['Content-Length'])
            post_data_bytes = self.rfile.read(content_length)
            post_data_str = post_data_bytes.decode("UTF-8")
            list_of_post_data = post_data_str.split('&')
            post_data_dict = {}

            for item in list_of_post_data:
                title, value = item.split('=')
                post_data_dict[title] = value
            
            email = post_data_dict['email']
            password = post_data_dict['your_pass']
            print(email)
            log_status = False
            with open("user-info.txt", "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if email == row['email'].strip() and password == row['password'].strip():
                        template_string = open(template_folder + "views/login.template.html").read().format(message = "You have been logged in as " + row['name'].strip())
                        open(rendered_folder + "login.html", "w").write(template_string)
                        self.path = rendered_folder + "login.html"
                        log_status = True
                        break
                
                if not log_status:
                    template_string = open(template_folder + "views/login.template.html").read().format(message = "Incorrect email or password")
                    open(rendered_folder + "login.html", "w").write(template_string)
                    self.path = rendered_folder + "login.html"




        return http.server.SimpleHTTPRequestHandler.do_GET(self)
            
            
if __name__ == '__main__':
    print (f"BLOG SERVER: I am running on http://localhost:{PORT}")
    my_server = socketserver.TCPServer(("", PORT), blog_server)
    my_server.serve_forever()
