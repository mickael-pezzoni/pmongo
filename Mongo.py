from pymongo import MongoClient, errors
import pprint
import datetime
from datetime import date
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

    def printCollection(self, base, _collectionName):
        db = self.client[base]
        content = str()
        collection = db[_collectionName]
        for elt in collection.find():
            content += pprint.pformat(elt)+'\n'
            """try:

            except:
                print('date invalid')"""
            if type(elt['date']) != datetime.datetime:
                print(elt['date'])
                try:
                    newDate = datetime.datetime.strptime(elt['date'], "%Y-%m-%d")
                    print(collection.update_one({'_id': elt['_id']}, {'$set': newDate}, upsert=False))
                except ValueError:
                    print('err')
                    """newDate = datetime.datetime.strptime(elt['date'], "%Y/%m/%d")
                    print(collection.update_one({'_id': elt['_id']}, {'$set': newDate}, upsert=False))"""
                except errors.WriteError:
                    print('WRITE_ERROR')
                    arrayDate = str(elt['date']).split('-')
                    # print(arrayDate)
                    # newDate = date(int(arrayDate[0]), int(arrayDate[1]), int(arrayDate[2]))
                    newDate = datetime.datetime(int(arrayDate[0]), int(arrayDate[1]), int(arrayDate[2]))
                    print(newDate)
                    print(collection.update_one({'_id': elt['_id']}, {'$set': { 'date': newDate}}, upsert=False))

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
