"""
Other utils for work with databases:
- mongo
"""
__author__ = 'neitro'


from pymongo import MongoClient


class MongoDB:
    _client = None

    def __init__(self, host: str='localhost', port: int=27017):
        """
        Init class

        :param host: host
        :param port: port

        """

        self._host = host
        self._port = port
        self._connect()

    def __del__(self):
        self._disconnect()

    def __exit__(self, exception_type, exception_value, traceback):
        self._disconnect()

    def _connect(self):
        """
        Connect with database

        :return:
        """

        connect_string = 'mongodb://{}:{}/'.format(
            self._host, str(self._port))
        self._client = MongoClient(connect_string)

    def _disconnect(self):
        """
        Disconnect database

        :return:
        """
        if self._client:
            self._client.close()
            self._client = None

    def get_db(self, db_name: str):
        """
        Get connect to database

        :param db_name: database's name

        :return:
        """

        return self._client[db_name]

    def get_collection(self, db_name: str, collection_name: str):
        """
        Get connect to database

        :param db_name: database's name
        :param collection_name: collection's name

        :return:
        """

        db = self.get_db(db_name)
        return db[collection_name]

    def insert(self, db_name: str, collection_name: str, values: list=[]):
        """
        Insert values in collection

        :param db_name:
        :param collection_name:
        :param values:

        :return:
        """
        collection = self.get_collection(db_name, collection_name)
        results = collection.insert(values)
        return [x.insert_id for x in results]

    def select(self,  db_name: str, collection_name: str, condition: dict={}):
        """

        :param db_name:
        :param collection_name:
        :param condition:

        :return:
        """
        return
