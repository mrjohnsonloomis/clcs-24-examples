from LibraryUser import LibraryUser
from Book import Book

info = ['mjohnson', 'password', 'Matt', 'Johnson', '4 Batchelder Road, Windsor CT', '6094397160']
user1 = LibraryUser(info)

book1 = Book('On Beauty','Zadie Smith')

user1.check_out(book1)
print(book1.is_out)

print(user1.get_book_history())