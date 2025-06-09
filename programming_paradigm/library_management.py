class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # خاص، كيحدد واش الكتاب مستعار ولا لا

    def check_out(self):
        """كيعلم بأن الكتاب مستعار"""
        self._is_checked_out = True

    def return_book(self):
        """كيعلم بأن الكتاب ترجع للمكتبة"""
        self._is_checked_out = False

    def is_available(self):
        """يرجع True إلا كان الكتاب متاح"""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # خاص، فيه جميع الكتب كأوبجيهات Book

    def add_book(self, book):
        """كيضيف كتاب للمكتبة"""
        self._books.append(book)

    def check_out_book(self, title):
        """كيستعير كتاب حسب العنوان"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book titled '{title}' is not available for checkout.")

    def return_book(self, title):
        """كيترجع كتاب للمكتبة"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book titled '{title}' is not checked out or not found.")

    def list_available_books(self):
        """كيتبع لائحة الكتب المتاحة"""
        for book in self._books:
            if book.is_available():
                print(book)
