from server_connection import Server
from datetime import datetime
class Loans:

    """
    Name: Aharon
    Date: 14-08-23
    Description: Book loan management class with 4 methods
    1) Loan a book,
    2) Return a book,
    3) Display all existing loans
    4) Display all late loans
    """

    server_connection = Server(
        'localhost,1433',
        'BookManagement',
        'sa',
        '12345678Aab',
        '/usr/local/lib/libmsodbcsql.17.dylib')

    def borrow_a_book(self, CustID, BookID, Loandate):
        """
        Name: Aharon
        Date: 14-08-23
        :param CustID: BookManagement DB CustomerID
        :param BookID: BookManagement DB BookID
        :param Loandate: Date of book loan
        :return: None
        """
        try:
            if datetime.strptime(Loandate, '%Y-%m-%d') <= datetime.today():
                with Server.connect_to_server(self.server_connection) as server_connection:
                    cursor = server_connection.cursor()
                    loans_data_query = """ SELECT COUNT(*) FROM Loans WHERE BookID = (?) and Returndate IS NULL """ # Checking if Loan exists and has not been return
                    cursor.execute(loans_data_query, BookID)

                    if cursor.fetchone()[0] == 0:
                        insert_new_loan_query = """ INSERT INTO Loans(CustID, BookID, Loandate) values (?, ?, ?) """ # Creating a new loan
                        cursor.execute(insert_new_loan_query, CustID, BookID, Loandate)
                        cursor.commit()
                        print(f'You have just borrowed a book, ID #{BookID}')

                    else:
                        print ('This book is currently unavailable to borrow')
            else:
                raise AssertionError('Invalid date, loandate can not be in the future')

        except Exception as e:
            print ('Error:',e)
        finally:
            Server.disconnect_from_server(self.server_connection)


    def return_book(self, BookID, Returndate):
        """
        Name: Aharon
        Date: 14-08-23
        :param BookID: BookManagement DB BookID
        :param Returndate: Date of book return
        :return: None
        """
        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()
                search_book_query = """ SELECT COUNT(*) FROM Loans WHERE BookID = (?) and Returndate IS Null """ # Checking BookID exists and has not been returned yet
                cursor.execute(search_book_query, BookID)

                if cursor.fetchone()[0] == 0:
                    print ('This book can not be returned')

                else:
                    get_loanDate_query = """ SELECT Loandate FROM Loans WHERE BookID = (?) """ # Checking for valid Returndate entry
                    cursor.execute(get_loanDate_query, BookID)
                    loandate = cursor.fetchone()[0]
                    date = loandate.isoformat()
                    if Returndate < date:
                        raise AssertionError('Return date can not be earlier than loandate')

                    else:
                        update_loan_query = """ UPDATE Loans SET Returndate = (?) WHERE BookID = (?) """ # Updating returnloan column in Loans table
                        cursor.execute(update_loan_query, Returndate, BookID)
                        cursor.commit()
                        print ('Book has been successfully returned')

        except Exception as e:
            print('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)


    def display_all_loans(self):
        """
        Name: Aharon
        Date: 14-08-23
        Description: Displays all loans in Loans table
        :return: 
        """""
        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()
                check_loans_query = """ SELECT COUNT(*) FROM Loans """  # Checking there are loans to display

                cursor.execute(check_loans_query)
                if cursor.fetchone()[0] == 0:
                    print('There are no loans to display')

                else:
                    get_loans_query = """ SELECT * from loans """  # Getting loans to display
                    cursor.execute(get_loans_query)
                    for i in cursor.fetchall():
                        if i[3] is None:
                            print(f'Customer ID: {i[0]}, Book ID: {i[1]}, LoanDate: {i[2]}, Returndate: Book not yet returned')
                            return ''

                        else:
                            print(f'Customer ID: {i[0]}, Book ID: {i[1]}, LoanDate: {i[2]}, ReturnDate: {i[3]}')
                        return ''

        except Exception as e:
            print('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)


    def display_late_loans(self):
        """
        Name: Aharon
        Date: 14-08-23
        :return: Displays all overdue loans, and loans returned passed due """

        def number_of_loan_days(bookID):
            """
            display_late_loans() Inner function
            :param BookID: BookManagement DB BookID
            :return: Number of loans days available for book """

            try:
                book_search_query = """ SELECT ID, Type FROM Books """
                cursor.execute(book_search_query)
                bookID_bookType_dict = {i[0]: i[1] for i in cursor.fetchall()}
                for key, value in bookID_bookType_dict.items():
                        if bookID == key:
                            if value == 1:
                                return 10
                            elif value == 2:
                                return 5
                            else:
                                return 2

            except Exception as e:
                print ('Error:', e)

        list_of_overdue_loans = []
        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()
                search_loan_query = """ SELECT BookID, DATEDIFF(DAY, Loandate, Returndate) 
                FROM Loans where Returndate is not Null """ # Getting BookID and days difference between loan and return for loans that have been returned

                cursor.execute(search_loan_query)
                loan_query_result = {i[0]: i[1] for i in cursor.fetchall()} # Converting result to a dictionary with BookID as key and number of days as value

                for key, value in  loan_query_result.items():
                    if number_of_loan_days(key) < value: # Calling inner function that return number of loan days based on book type
                        list_of_overdue_loans.append(key)
                    pass

                get_loan_query = """ SELECT BookID, DATEDIFF(DAY, Loandate, GETDATE()) 
                FROM Loans WHERE Returndate is Null """ # Getting BookID and days difference between loandate and todays date for loans that have not been returned
                cursor.execute(get_loan_query)

                dictionary_result2 = {i[0]: i[1] for i in cursor.fetchall() if cursor.fetchall() != 0} # Converting result to a dictionary with BookID as key and number of days as value

                for key, value in dictionary_result2.items():
                    if number_of_loan_days(key) < value:
                        list_of_overdue_loans.append(key) # Calling inner function that returns number of loan days available based on book type

                if len(list_of_overdue_loans) != 0:
                    list_of_late_loans =[]
                    search_loan_query = """ SELECT * FROM Loans """
                    cursor.execute(search_loan_query)
                    for row in cursor.fetchall():
                        if any(i in row for i in list_of_overdue_loans) and row not in list_of_late_loans:
                            list_of_late_loans.append(row)

                    for i in list_of_late_loans:
                        print (f'Late loan - CustomerID: {i[0]}, BookID: {i[1]}, Loan-date: {i[2]}, Return-date: {i[3]}')
                    return ' '

        except Exception as e:
            print('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)
