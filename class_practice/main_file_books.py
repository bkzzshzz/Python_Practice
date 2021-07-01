from books import Books
#creating an object; object is an instance of a class
book1 = Books("Anuradha", "Bijay Malla", 148, True)
book2 = Books("Pratibaddha", "Diamond Shumshere", 240, True)
book3 = Books("Sapiens", "Yuval", 500, False)
#accessing classes
print(book1.title)
if book1.is_fiction:
    print(book1.title + " is a fiction")
if book2.is_fiction:
    print(book1.title + " is a fiction")
if book3.is_fiction:
    print(book2.title + " is a fiction")
else:
    print(book3.title + " is not a Fiction")
