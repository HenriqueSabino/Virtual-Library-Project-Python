class Student:
    def __init__(self, student_id: str, first_name: str, last_name: str, email: str, rental_history: list):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.rental_history = rental_history

    def rent_book(self, book):
        self.rental_history.append(book)

    def return_book(self, book):
        self.rental_history.remove(book)