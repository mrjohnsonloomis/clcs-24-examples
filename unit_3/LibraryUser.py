class LibraryUser:

    id_counter = 1

#Constructor -- takes in a list of info as a parameter
    def __init__(self, info, email):
        '''info is a list read in from a line from a form on the website (which is stored in a csv file)'''
        self.username = info[0]
        self.password = info[1]
        self.first_name = info[2]
        self.last_name = info[3]
        self.address = info[4]
        self.phone = info[5]
        self.is_active = True
        self.id_num = LibraryUser.id_counter
        self.has_late = False
        self.books_out = []
        self.book_history = []
        self.email = email

        #increases the ID coutner to create a new, unique ID each time the constructor is called
        LibraryUser.id_counter += 1


#Instance Methods

    def check_out(self, book):
        '''checks out a book @param is a book object'''
        if book.is_out == False:
            book.is_out = True

            #updates the list of books out as well as user history
            self.books_out.append(book)
            self.book_history.append(book)
        
    
    def is_late(self):
        '''sets whether a user has a late item and owes a fee'''
        for books in self.books_out:
            if books.is_late: self.has_late = True

    def return_book(self, book):
        '''returns a book'''
        if book in self.books_out:
            self.books_out.remove(book)
        else:
            print('Error: Patron does not have that book checked out.')

    def get_book_history(self):
        '''returns a list of book titles user has taken out'''
        str_books = []
        for book in self.book_history:
            str_books.append(book.get_title())
        return str_books