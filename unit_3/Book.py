class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_out = False
        self.is_late = False

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_title(self):
        return self.title