from pymongo import MongoClient
# from config.config import Config


# NOSQL_USERNAME = Config.NOSQL_USERNAME
# NOSQL_PASSWORD = Config.NOSQL_PASSWORD
# NOSQL_HOST = Config.NOSQL_HOST
# NOSQL_PORT = Config.NOSQL_PORT
# DB_NAME = Config.DB_NAME


class MongoConn:

    __uri_local = "mongodb://localhost:27017/"
    __db_name = "studentManagement"

    def __init__(self) -> None:
        """ 
        Initialize the MongoConn class.

        :param uri: MongoDB connection string URI.
        :param db_name: Name of the database to connect to.
        """
        self.uri = self.__class__.__uri_local
        self.db_name = self.__class__.__db_name
        self.client = None
        self.db = None

    def connect(self):
        """
        Connect to the MongoDB database.

        :return: True if connection is successful, False otherwise.
        """
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            return self.db
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return False

    def create_db(self, new_db_name):

        try:
            self.client[new_db_name]
            print(f"Database '{new_db_name}' created.")
        except Exception as e:
            print(f"Error creating database: {e}")

    def create_collections(self, collection_name):
        try:
            db_name = self.client[self.db_name]
            db_name[collection_name]
        except Exception as e:
            print(f"Error creating collection: {e}")
