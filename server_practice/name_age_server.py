import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/name_age_form.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/verify':
            content_length = int(self.headers['Content-Length'])
            post_data_bytes = self.rfile.read(content_length)
            post_data_str = post_data_bytes.decode("UTF-8")
            list_of_post_data = post_data_str.split('&')
            post_data_dict = {}

            for item in list_of_post_data:
                variable, value = item.split('=')
                post_data_dict[variable] = value

            
            age = int(post_data_dict['age'])
            first_name = str(post_data_dict['fname'])
            eligibility = ""
            if age > 18:
                eligibility = "eligible"
            else:
                eligibility = "not eligible"
            new_file = open("verify.html").read().format(fname= first_name, eligible = eligibility)
            index = open("verify2.html", "w").write(new_file)


            self.path = "verify2.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
        

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Start the server
my_server.serve_forever()