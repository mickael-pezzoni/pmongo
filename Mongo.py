from pymongo import MongoClient
import pprint


class Mongo:
    """Classe pour une connection à une base mongo """

    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.client = MongoClient('mongodb://'+user+':'+password+'@'+host+':'+port+'/')
    
    def showDataBase(self):
        for db in self.client.database_names():
            print("*", db)

    def printCollection(self, base, collectionName):
        db = self.client[base]
        content = str()
        collection = db[collectionName]
        for elt in collection.find():
            content += pprint.pformat(elt)+'\n'
        return content

    def showListCollection(self, base):
        db = self.client[base]
        nbCollection = 0
        for collection in db.collection_names():
            nbCollection += 1
            print("{} : {}".format(nbCollection, collection))
        print("\n{} collections trouvées".format(nbCollection))

    def exportAllCollectioni(self, base):
        db = self.client[base]
        nbCollection = 0
        for collection in db.collection_names():
            nbCollection += 1
            with open(collection + ".json", "w+") as fichier:
                print("Export " + collection + " ...")
                fichier.write(self.printCollection(base, collection))
        print("Export finit")

    def exportOneCollection(self, base, collection):
        db = self.client[base]
        with open(collection + ".json", 'w+') as fichier:
            print("Export " + collection + " ...")
            fichier.write(self.printCollection(base, collection))
            print("Export finit")
