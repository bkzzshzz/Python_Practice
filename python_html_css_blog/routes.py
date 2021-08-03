class Route:

    def __init__(self, list_of_paths, redirect_path_list):
        self.list_of_paths = list_of_paths
        self.redirect_path_list = redirect_path_list
    
    def add_path_to_list(input_path, return_url):
        pass

    def register_url(input_path):
        pass


if __name__ == '__main__':
    all_paths = ["/", "/my-contact.html", "/blog-posts/", "/images/", "/poems", "/poems.html", "/programming-journey", "/programming-journey.html", "/my-cv.html", "/my-cv", "/cv", "/home.html", "/home", "/book-reviews", "/book-reviews.html", "/gallery", "/gallery.html"]
    map_input_output = {
        "/" : "/home.html",
        "/my-contact.html" : "/404.html",
        "/blog-posts/" : "/list_of_blogs.html",
        "/images/" : "/401.html",
        "/programming-journey" : "/programming-journey.html",
        "/programming-journey.html" : "/programming-journey.html",
        "/poems" : "/poems.html",
        "/poems.html" : "/poems.html",
        "/my-cv.html" : "/my-cv.html", 
        "/my-cv" : "/my-cv.html", 
        "/cv" : "/my-cv.html", 
        "/home.html" : "/home.html", 
        "/home" : "/home.html",
        "/book-reviews" : "/book-reviews.html", 
        "/book-reviews.html": "/book-reviews.html", 
        "/gallery" : "/gallery.html", 
        "/gallery.html" : "/gallery.html"

    }

    route_instance = Route(all_paths, map_input_output)


    

