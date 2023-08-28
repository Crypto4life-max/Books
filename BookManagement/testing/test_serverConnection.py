import pytest
import server_connection

class TestConnection():


    def test_serverConnection(self):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing manually connecting to server
        :return: None
        """
        connection = sql_connection.Server('localhost,1433', 'BookManagement', 'sa', '12345678Aab', '/usr/local/lib/libmsodbcsql.17.dylib')
        conn = connection.connect_to_server()
        assert conn is not None


    def test_disconnect_from_server(self):
        """
        Name: Aharon
        Date: 16-08-23
        Description: Testing manually disconnecting from server
        :return: None
        """
        connection = sql_connection.Server('localhost,1433', 'BookManagement', 'sa', '12345678Aab', '/usr/local/lib/libmsodbcsql.17.dylib')
        conn = connection.disconnect_from_server()
        assert conn is None



if __name__ == '__main__':
    pass




