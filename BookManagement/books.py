from server_connection import Server
class Books:

    """
    name: aharon
    date: 14-08-23
    description: Book managment class with 4 methods
    1) Adds a book from DB,
    2) Removes a book from DB,
    3) Displays all existing books,
    4) Finds a specific book by name
    """

    server_connection = Server(
        'localhost,1433',
        'BookManagement',
        'sa',
        '12345678Aab',
        '/usr/local/lib/libmsodbcsql.17.dylib')

    def __init__(self,name, author, year_published, type: int):
        self.__name = name
        self.__author = author
        self.__year_published = year_published
        if type == 1 or type == 2 or type == 3:
            self.__type = type
        else:
            raise ValueError('Type must be 1, 2 or 3')


    def add_new_book(self):
        """
        name: aharon
        date: 14-08-23
        description: Adds a book to BookManagement database
        """
        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()

                check_book_query = """ SELECT COUNT(*) from Books WHERE Name = ? """
                insert_book_query = """ INSERT INTO Books values (?, ?, ?, ?) """

                cursor.execute(check_book_query, self.__name)
                if cursor.fetchone()[0] != 0:
                    print ('Error: Book already exists in library')

                else:
                    cursor.execute(insert_book_query, self.__name, self.__author, self.__year_published, self.__type)
                    cursor.commit()
                    print ('Book has been successfully added to library')

        except Exception as e:
            print ('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)


    def remove_book(self, id):
        """
        name: aharon
        date: 14-08-23
        description: Removes a book by ID from Books table
        :param id: BookManagement DB BookID
        :return: None
        """

        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()

                check_bookID_query = """  SELECT COUNT (*) From Books Where ID = (?)  """  # Checking if bookID exists
                check_loan_query = """  SELECT COUNT (*) From Loans Where BookID = (?) """  # Checking if there is a loan associated wth bookID
                delete_loan_query = """ DELETE FROM Loans WHERE BookID = (?) """ # Deleting loan associated with BookID.
                delete_book_query = """ DELETE FROM Books WHERE ID = (?) """ # Removing book from DB

                cursor.execute(check_bookID_query, id)
                if cursor.fetchone()[0] != 0:
                    cursor.execute(check_loan_query, id)
                    if cursor.fetchone()[0] != 0:
                        cursor.execute(delete_loan_query, id)
                        cursor.execute(delete_book_query, id)
                        cursor.commit()
                        print('Book has been removed successfully from library')

                    else:
                        cursor.execute(delete_book_query, id)
                        cursor.commit()
                        print('Book has been removed successfully from library')\

                else:
                    print ('BookID invalid')

        except Exception as e:
            print ('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)


    def display_all_books(self):
        """
        name: aharon
        date: 14-08-23
        :return: Display of all books in library
        """

        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()

                search_count_book_query = """ SELECT COUNT(*) FROM Books """
                cursor.execute(search_count_book_query)
                if cursor.fetchone()[0] == 0:
                    print ('Books table is empty')

                else:
                    search_book_query = """ SELECT * FROM Books """
                    cursor.execute(search_book_query)
                    for i in cursor.fetchall():
                        print (f'ID: {i[0]}, Name: {i[1]}, Author: {i[2]}, Publish Year: {i[3]}, Loan Type: {i[4]}')
                return ''

        except Exception as e:
            print('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)


    def find_book_by_name(self, book_name):
        """
        name: Aharon
        date: 14-08-23
        :param name: BookManagement DB book name
        :return: Book by name
        """
        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()
                search_count_book_query = """ SELECT COUNT(*) FROM Books WHERE Name = (?) """
                cursor.execute(search_count_book_query, book_name)
                if cursor.fetchone()[0] == 0:
                    print('This book does not exist')

                else:
                    search_book_query = """ SELECT * FROM Books WHERE Name = (?) """
                    cursor.execute(search_book_query, book_name)
                    for i in cursor.fetchall():
                        print (f'The book you have searched for is - BookID: {i[0]}, Name: {i[1]}, Author: {i[2]}, Year published: {i[3]}, Loan type: {i[4]}')
                return ''

        except Exception as e:
            print('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)

