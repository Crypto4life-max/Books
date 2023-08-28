from server_connection import Server
class Customer:

    """
    Name: Aharon
    Date: 14-08-23
    Description: Customer management class with 4 methods
    1) Adds a new customer,
    2) Removes an existing customer,
    3) Displays all existing customers,
    4) Finds a specific customer by name
    """

    server_connection = Server(
        'localhost,1433',
        'BookManagement',
        'sa',
        '12345678Aab',
        '/usr/local/lib/libmsodbcsql.17.dylib')


    def __init__(self, name, city, age):
        self.__name = name
        self.__city = city
        self.__age = age


    def add_new_customer(self):
        """
        Name: Aharon
        Date: 14-08-23
        Description: Adds a new customer containing (name, city, age) to BookManagement DB Customers table
        :return: None
        """
        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()
                check_customer_by_name_query = """ SELECT COUNT(*) from Customers WHERE Name = (?) """ # Checking if customer name exists

                cursor.execute(check_customer_by_name_query, self.__name)
                if cursor.fetchone()[0] != 0:
                    print ('Error: Customer already exists')

                else:
                    insert_customer_query = """  INSERT INTO Customers values (?, ?, ?) """  # Adding customer to Customers table in DB
                    cursor.execute(insert_customer_query, self.__name, self.__city, self.__age)
                    cursor.commit()
                    print('Customer successfully added')

        except Exception as e:
            print('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)


    def remove_customer(self, customer_id):
        """
        name: Aharon
        date: 15-08-23
        description: Removes a customer from BookManagement DB by customerID
        :param id: BookManagement DB CustomerID
        :return: None
        """
        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()
                check_customer_query = """ SELECT COUNT(*) FROM Customers WHERE ID = (?) """ # Checking if customerID exists in Customers table

                cursor.execute(check_customer_query, customer_id)
                if cursor.fetchone()[0] == 0:
                    print('This customer does not exists')
                else:
                    delete_customer_query = """ DELETE FROM Customers WHERE ID = (?) """ # Deleting customer from Customers table in DB
                    cursor.execute(delete_customer_query, customer_id)
                    cursor.commit()
                    print('Customer has been removed successfully')

        except Exception as e:
            print('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)



    def display_all_customers(self):
        """
        Name: Aharon
        Date: 14-08-23
        :return: Displays all existing customers
        """
        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()
                check_customer_query = """ SELECT COUNT(*) FROM Customers """ # Checking if customers table contains customers

                cursor.execute(check_customer_query)
                if cursor.fetchone()[0] == 0:
                    print('Customer table is empty')

                else:
                    get_customers_query = """ SELECT * from Customers """ # Getting all customers from Customers table
                    cursor.execute(get_customers_query)
                    for i in cursor.fetchall():
                        print (f'Customer ID: {i[0]}, Name: {i[1]}, City: {i[2]}, Age: {i[3]}')
                return ''

        except Exception as e:
            print('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)


    def find_customer_by_name(self, name):
        """
        Name: Aharon
        Date: 15-08-23
        :param name: BookManagement DB book name
        :return: Customer
        """
        try:
            with Server.connect_to_server(self.server_connection) as server_connection:
                cursor = server_connection.cursor()
                check_customer_query = """ SELECT COUNT(*) FROM Customers WHERE Name = (?) """ # Checking if customer name exists in Customers table

                cursor.execute(check_customer_query, name)
                if cursor.fetchone()[0] == 0:
                    print('This customer does not exist')

                else:
                    get_customer_query = """ SELECT * FROM Customers WHERE Name = (?) """ # Getting customer details from Customers table
                    cursor.execute(get_customer_query, name)
                    for i in cursor.fetchall():
                        print (f'The customer you have searched for - Customer ID: {i[0]}, Name: {i[1]}, City: {i[2]}, Age: {i[3]}')
                return ''

        except Exception as e:
            print('Error:', e)
        finally:
            Server.disconnect_from_server(self.server_connection)


