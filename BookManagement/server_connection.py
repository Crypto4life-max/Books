import pyodbc as odbc
class Server:


    def __init__(self,server,database,username,password,driver):
        self.__server = server
        self.__database = database
        self.__username = username
        self.__password = password
        self.__driver = driver
        self.__connection = None

    def connect_to_server(self):
        """
        Name: Aharon
        Date: 14-08-23
        Description: manually connects to server
        :return: Server connection
        """
        connection_string = f"DRIVER={{{self.__driver}}};SERVER={self.__server};DATABASE={self.__database};UID={self.__username};PWD={self.__password}"
        try:
            self.__connection = odbc.connect(connection_string)
            print ('Server connection successful')

        except Exception as e:
            print ('Error:',e)

        return self.__connection


    def disconnect_from_server(self):
        """
        Name: Aharon
        Date: 14-08-23
        Description: manually closes server connection
        :return: None
        """
        try:
            if self.__connection is not None:
                self.__connection.close()
                print ('Server connection closed')
            else:
                print('Connection was already closed')

        except Exception as e:
            print ('Error:', e)



