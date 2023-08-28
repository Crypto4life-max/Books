import pytest
from server_connection import Server
@pytest.fixture
def connection():
    connect = Server('localhost,1433', 'BookManagement', 'sa', '12345678Aab', '/usr/local/lib/libmsodbcsql.17.dylib')
    connection = connect.connect_to_server()
    yield connection



if __name__ == '__main__':
    pass
