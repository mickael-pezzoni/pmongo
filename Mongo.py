from pymongo import MongoClient
import pprint

class Mongo:
    """Classe pour une connection à une base mongo """
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = MongoClient(self.host,self.port)
    
    def showDataBase(self):
        for db in self.client.database_names():
            print("*",db)
    
    def printCollection(self, base, collectionName):
        db = self.client[base]
        collection = db[collectionName]
        for elt in collection.find():
            pprint.pprint(elt)
    
    def showListCollection(self,base):
        db = self.client[base]
        nbCollection = 0
        for collection in db.collection_names():
            nbCollection+=1
            print("{} : {}".format(nbCollection,collection))
        print("\n{} collections trouvées".format(nbCollection))
