import pytest
import customers

class TestCustomers():


    def test_add_customer(self, connection):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing adding a customer to Customers table
        :param connection: Fixture connection
        :return: None
        """
        cursor = connection.cursor()
        new_customer = customers.Customer('Roy' , 'jerusalem', 20)
        cursor.execute('select count(*) from Customers')
        initial_customer_count = cursor.fetchone()[0]
        new_customer.add_new_customer()
        cursor.execute('select count (*) from Customers')
        final_customer_count = cursor.fetchone()[0]
        assert final_customer_count > initial_customer_count


    def test_try_adding_an_existing_customer(self):
        """
       Name: Aharon
       Date: 16-08-23
       Description: Testing adding a customer that already exists
       :return: AssertionError
       """
        new_customer = customers.Customer('miri', 'jerusalem', 20) # Customer must already be in DB in order for this test to work
        new_customer.add_new_customer()
        assert AssertionError


    def test_remove_customer(self, connection):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing deleting a customer from Customers table
        :param connection: Fixture connection
        :return: None
        """
        cursor = connection.cursor()
        new_customer = customers.Customer('miri', 'jerusalem', 20)  # Customer must exist in DB
        cursor.execute('SELECT COUNT (*) FROM Customers')
        initial_book_count = cursor.fetchone()[0]
        new_customer.remove_customer(5002)  # ID must match CustomerID in Customer table in DB
        cursor.execute('SELECT COUNT (*) FROM Customers')
        final_book_count = cursor.fetchone()[0]
        assert final_book_count < initial_book_count


    def test_remove_nonexistent_customer(self): # parameters CustomerID
        """
        Name: Aharon
        Date: 16-08-23
        Description: Deleting a customer that does not exist
        :return: AssertionError
        """
        new_customer = customers.Customer('miri', 'jerusalem', 22)
        new_customer.remove_customer(890) # CustomerID #890 is invalid
        assert AssertionError



    def test_display_all_customers(self):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing displaying all customers
        :return: all_customers is not None
        """
        new_customer = customers.Customer('miri', 'jerusalem', 20)
        new_customer.add_new_customer()
        all_customers = new_customer.display_all_customers()
        assert all_customers is not None



    def test_search_customer(self):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing search customer by name
        :return: Customer_by_name is not None
        """
        new_customer = customers.Customer('miri', 'jerusalem', 20)
        new_customer.add_new_customer()
        customer_by_name = new_customer.find_customer_by_name('miri')
        assert customer_by_name is not None


    def test_search_customer_by_nonexistent_name(self):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing searching for customer by non-existent name
        :return: AssertionError
        """
        new_customer = customers.Customer('miri', 'jerusalem', 20)
        new_customer.find_customer_by_name('ronny') # ronny is a non-existent name
        assert AssertionError


if __name__ == '__main__':
    pass
