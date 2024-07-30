
from db.mongo_conn import MongoConn


class ProductDataLayer(MongoConn):

    __collection_name = "product"

    def __init__(self) -> None:

        super().__init__()
        self.connect()

    def create_collections(self):
        super().create_collections(self.__class__.__collection_name)

    def list_all_documents(self):
        """
        List all documents in the specific collection defined by __collection_name.

        :return: List of documents in the specified collection.
        """
        dic = []
        try:
            # Access the specific collection
            collection = self.db[self.__class__.__collection_name]
            # Retrieve all documents in the collection
            documents = collection.find()
            for doc in documents:
                dic.append(doc)
            return dic
        except Exception as e:
            print(f"Error listing documents: {e}")
            return []

    def insert_document(self, document):
        """
        Insert a document into the specified collection.

        :param collection_name: Name of the collection to insert the document into.
        :param document: The document to insert.
        :return: None
        """
        try:
            collection = self.db[self.__class__.__collection_name]
            collection.insert_one(document)
        except Exception as e:
            print(f"Error inserting document: {e}")


document = {"id": 27,
            "name": "Hung Thinh",
            "age": 23,
            "city": "Bac Lieu"}

product_data_layer = ProductDataLayer()
a = product_data_layer.insert_document(document)
b = product_data_layer.list_all_documents()

for i in b:

    print(i)
#  export PYTHONPATH=$PYTHONPATH:/Users/macos/Downloads/WORKSPACE/e-commerce-project/src/db
