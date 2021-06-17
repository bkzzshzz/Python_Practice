# Python server practice

### Learned

1. __POST__ request

    This request sends the data to the server in a designated format.
2. __GET__ request

    This request appends the data to the url.

    The following program is an example of get request.
    ```python
    import requests
    r = requests.get('https://api.github.com/')
    print(r.json())
    print(r.text)
    ```
    The POST method is just writing post instead of get.

    ```python
    import requests
    r = requests.post('https://api.github.com/')
    print(r.json())
    print(r.text)
    ```
3. The python backend to serve a simple html file:
    ```python
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class server(BaseHTTPRequestHandler):

        def do_GET(self):
            if self.path == "/":
                self.path = "for_response.html"
                html_file = open(self.path).read()
                self.send_response(200)
            
            self.end_headers()
            self.wfile.write(bytes(html_file, 'utf-8'))
    PORT = 8000
    page = HTTPServer(('localhost', PORT), server)
    page.serve_forever()
    ```
    _http.server_ is the package that is used in web handling for http.

    _HTTPServer_ and _BaseHTTPRequestHandler_ are the modules that help in passing data to and fro server and client.

    `class server(BaseHTTPRequestHandler):` creates a class that acquires all the attributes of _BaseHTTPRequestHandler_ module.

    `def do_GET(self)` initialises the __GET__ request for the server.

    ```python
    if self.path == "/":
        self.path = "for_response.html"
    ```
    The _key_ thing to note here is that the root page is always `"/"`. And this couple of lines check is the root page is called and displays _for_response.html_ file.

    _Response 200 means OK and response 404 means the page is not found._

    `self.wfile.write(bytes(html_file, 'utf-8'))` converts the html_file to bytes after encoding it with __UTF-8__.
    
    `page = HTTPServer(('localhost', PORT), server)` passes PORT and the return response from server class. `page.serve_forever()` runs the server.
4. The _socketserver_ module simplifies the task of writing network servers. (That's all I need to know for now)
5. For Q.7 of June 15-16th goals, we need to make three separate html files: one for Eligible, one for Not-Eligible and the last one with the form. The form's method must be __POST__ as it sends the data to the server in the encoded format.
6. When [Server.py](https://github.com/bkzzshzz/Python_Practice/blob/master/server_practice/server.py) is run and the _localhost:PORT_ is called, it is a _GET_ request. But when the _submit_ button is pressed in the form page, the POST method is requested and the form data is sent back to the _Server.py_. __This code needs to be revisited again__.
7. [blog.py](https://github.com/bkzzshzz/Python_Practice/blob/master/server_practice/blog/blog.py) file runs the _GET_ method as we need to pass the input appended after the root url. 

### Key Notes

1. If one _PORT_ is engaged then, just alter the port value, run the program and to the url with the same port. 
2. Ctrl+Shift+i shows all the requests that occur in a page. 








