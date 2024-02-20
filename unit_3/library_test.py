from LibraryUser import LibraryUser
from Book import Book

info = ['mjohnson', 'password', 'Matt', 'Johnson', '4 Batchelder Road, Windsor CT', '6094397160']
user1 = LibraryUser(info, 'matthew_johnson@loomis.org')

book1 = Book('On Beauty','Zadie Smith')

print(user1.email)
user1.check_out(book1)
print(book1.is_out)

print(user1.get_book_history())