from psycopg2 import OperationalError, connect


class Connection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = self._create_connection(self.database, self.user, self.password, self.host, 5432)

    @staticmethod
    def _create_connection(db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            connection = connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
        except OperationalError as error:
            print("The error", error, "occurred")
        return connection

    def execute_query(self, query, data, fetching=False):
        self.connection.autocommit = True
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, data)
            if fetching:
                result = cursor.fetchall()
                return result
        except OperationalError as error:
            print("The error", error, "occurred")

    def get_categories(self):
        query = "SELECT * FROM categories"
        return self.execute_query(query, None, fetching=True)

    def close_connection(self):
        if self.connection:
            self.connection.close()
