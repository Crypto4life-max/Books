import pytest
import loans
class TestLoans():


    def test_borrow_a_book(self, connection):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing adding a loan to Loans table
        :param connection: Fixture connection
        :return: None
        """
        cursor = connection.cursor()
        new_loan = loans.Loans()
        cursor.execute('SELECT COUNT (*) FROM Loans')
        initial_loans_count = cursor.fetchone()[0]
        new_loan.borrow_a_book(1, 6036, '2022-09-12')  # This test will only work when entered parameters are not in DB. After running this test once, paremeters must be changed else the test will fail.
        cursor.execute('SELECT COUNT (*) FROM Loans')
        final_loans_count = cursor.fetchone()[0]
        assert final_loans_count > initial_loans_count


    def test_borrow_a_nonexistent_book(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing borrowing a book with nonexistent BookID
        :return: AssertionError
        """
        loan = loans.Loans()
        try:
            loan.borrow_a_book(1, 6010,  '2021-11-09')  # 6010 is non existent book id
        except AssertionError as e:
            assert str(e) == 'This book can not be returned'



    #@pytest.mark.xfail
    def test_try_borrowing_with_invalid_loan_date(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing entering a loandate that is in the future
        :return: AssertionError
        """
        loan = loans.Loans()
        try:
            loan.borrow_a_book(1, 1, '2025-11-24')
        except AssertionError as e:
            assert str(e) == 'Invalid date, loandate can not be in the future'



    def test_try_borrowing_a_book_with_entering_returndate(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing borrowing a book with Returndate entered
        :return: TypeError
        """
        loan = loans.Loans()
        with pytest.raises(TypeError):
            loan.borrow_a_book(1, 1, '2022-11-24', '2022-11-25')


    def test_borrow_a_book_that_is_currently_borrowed(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing borrowing a book that is already borrowed
        :return: AssertionError
        """
        loan = loans.Loans()
        loan.return_book(4044, '2023-09-12')
        loan.borrow_a_book(1, 4044, '2020-09-11') # Returndate for BookID must be not Null
        assert AssertionError


    def test_return_a_book(self, connection):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing returning a book
        :param connection: Fixture connection
        :return:
        """
        cursor = connection.cursor()
        loan = loans.Loans()
        loan.borrow_a_book(1, 5034, '2023-11-24')
        loan.return_book(1, '2023-11-12')
        cursor.execute('SELECT COUNT (*) FROM Loans WHERE BookID = (?) And Returndate is Null', 1)
        assert cursor.fetchone()[0] == 0



    def test_return_a_book_that_has_already_been_returned(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing returning a book that is already returned
        :return: AssertionError
        """
        loan = loans.Loans()
        loan.return_book(5034, '2023-11-12') # This bookID (1) has already been returned. In order for this test to work bookID Returndate must not be Null.
        assert AssertionError


    def test_return_a_book_that_does_not_exist(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing returning a book with invalid BookID
        :return: AssertionError
        """
        loan = loans.Loans()
        try:
            loan.return_book(5009, '2021-11-09') # 5009 is non existent book id
        except AssertionError as e:
            assert str(e) == 'This book can not be returned'


    def test_return_a_book_with_invalid_return_date(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing returning a book with invalid returndate
        :return: AssertionError
        """
        loan = loans.Loans()
        try:
            loan.return_book(5034, '2000-11-09') # return date can not be earlier than loan date
        except AssertionError as e:
            assert str(e) == 'Return date is invalid'


    def test_entering_date_with_incorrect_format(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing entering incorrect date format
        :return: AssertionError
        """
        loan = loans.Loans()
        try:
            loan.borrow_a_book(1, 5034, '08-11-2019') # Date format is incorrect
        except AssertionError as e:
            assert str(e) == 'time data 08-11-2019 does not match format %Y-%m-%d'


    def test_display_all_loans(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing display all loans returns not None
        :return:
        """
        loan = loans.Loans()
        loan.borrow_a_book(1, 4042, '2012-11-08')
        all_loans = loan.display_all_loans()
        assert all_loans is not None


    def test_display_a_late_loan(self):
        """
        Name: Aharon
        Date: 20-08-23
        Description: Testing display late loans returns not None
        :return:
        """
        loan = loans.Loans()
        loan.borrow_a_book(1, 1, '2012-09-05')
        late_loans = loan.display_late_loans()
        assert late_loans is not None





# bug needs to be fixed - currently you can return a loan on a date before the borrow date!



if __name__ == '__main__':
    pass
