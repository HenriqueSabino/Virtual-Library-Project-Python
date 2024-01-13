class Book:
    def __init__(self, title, author, isbn, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def rent_book(self):
        if self.status == 'Available':
            self.status = 'Rented'
            return True
        return False

    def return_book(self, new_status):
        if self.status == 'Rented':
            self.status = new_status
            return True
        return False