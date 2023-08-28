import loans
from books import Books
from customers import Customer
from loans import Loans
import server_connection as Server
import pyodbc



cust = Customer('Lori', 'Los Angeles', 31)

book1 = Books('Longest road', 'Bob Rice', '1993', 1)
book2 = Books('Header ups', 'Rollin stone', '1988', 3)
book3 = Books('The darkest hour', 'Slim biskit', '1870', 2)
book4 = Books('A long night', 'Rockefeller', '1928', 1 )
book5 = Books('Catch me if you can', 'Robert idk', '2020', 2)
loan = loans.Loans()
cust1 = Customer('Rina', 'Jerusalem', 30)
print()
if __name__ == '__main__':
    loan.return_book(6036, '2023-09-12')
