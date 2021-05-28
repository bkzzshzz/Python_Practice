#creating own datatype
class Books:
    def __init__(self, title, author, number_of_pages, is_fiction):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_fiction = is_fiction

    def is_lengthy(self):
        if self.number_of_pages >= 250:
            return True
        else:
            return False