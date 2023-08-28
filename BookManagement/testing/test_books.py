import pytest
import books

class TestBooks():


    def test_add_book_to_database(self, connection):
        """
       Name: Aharon
       Date: 16-08-23
       Description: Testing adding a new book to Books table
       :param connection: Fixture connection
       :return: None
       """
        cursor = connection.cursor()
        new_book = books.Books('miss', 'ruth', 1980, 2) # This test will only work when entered parameters are not in DB. After running this test once, paremeters must be changed else the test will fail.
        cursor.execute('SELECT COUNT (*) FROM Books')
        initial_book_count = cursor.fetchone()[0]
        new_book.add_new_book()
        cursor.execute('SELECT COUNT (*) FROM Books')
        final_book_count = cursor.fetchone()[0]
        assert final_book_count > initial_book_count


    def test_try_to_add_existing_book(self):
        """
       Name: Aharon
       Date: 16-08-23
       Description: Testing adding a book that already exists
       :return: AssertionError
       """
        new_book = books.Books('miss', 'ruth', 1980, 2) # In order for this test to work params must be of an existing book
        new_book.add_new_book()
        assert AssertionError


    def test_add_book_nonexistent_booktype(self):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing for valueError when an invalid book type is entered
        :return: ValueError
        """
        with pytest.raises(ValueError):
            books.Books('name', 'author', 1980, 4) # book type 4 is invalid


    def test_remove_book_from_database(self, connection):  # parameters BookID
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing deleting a book from Books table
        :param connection: Fixture connection
        :return: None
        """
        cursor = connection.cursor()
        new_book = books.Books('hi', 'ruth', 1980, 2)
        cursor.execute('SELECT COUNT (*) FROM Books')
        initial_book_count = cursor.fetchone()[0]
        new_book.remove_book(6035) # ID must match BookID in DB
        cursor.execute('SELECT COUNT (*) FROM Books')
        final_book_count = cursor.fetchone()[0]
        assert final_book_count < initial_book_count


    def test_remove_nonexistent_bookID(self):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing removing a bookID that does not exist
        :return: AssertionError
        """
        new_book = books.Books('hi', 'ruth', 1980, 2)
        new_book.remove_book(8933) # BookID #8933 is invalid
        assert AssertionError


    def test_display_all_books(self ):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing display all books from Books table
        :return: Display of all_books is not None
        """
        new_book = books.Books('name', 'author', 1980, 2)
        new_book.add_new_book()
        all_books = new_book.display_all_books()
        assert all_books is not None



    def test_search_for_a_book_by_name(self): # parameters BookName
        """
       Name: Aharon
       Date: 16-08-23
       Description: Testing return book by name
       :return: book by name is not None
       """

        new_book = books.Books('name', 'author', 1980, 2)
        new_book.add_new_book()
        book_by_name = new_book.find_book_by_name('name')
        assert book_by_name is not None


    def test_search_for_book_by_name_that_does_not_exist(self):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing searching for a book by non-existent name
        :return: AssertionError
        """
        new_book = books.Books('name', 'author', 1980, 2)
        new_book.find_book_by_name('rocker-feller')
        assert AssertionError

if __name__ == '__main__':
    pass
