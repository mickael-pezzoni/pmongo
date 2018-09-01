#!/usr/bin/python3

import datetime as date
from random import randint
from pymongo import MongoClient
import pprint
import argparse


def printCollection(collection):
        for elt in collection.find():
            pprint.pprint(elt)

HOST = ''
PORT = 27017
client = MongoClient(HOST,PORT)

parser = argparse.ArgumentParser(description="Gestion base mongodb")
parser.add_argument("-D",'--db', help="Base de donnée", default="apiwatchTest", metavar='Base')
parser.add_argument("-p", help="Affiche la collections indiquée",metavar="COLLECTION")
parser.add_argument("-c","--collection", action="store_true", help="Affiche les collections de la base")
parser.add_argument("--dbs", action="store_true", help="Affiche les bases")
args = parser.parse_args()


if(args.dbs and args.db):
	dbs = client. database_names()
	for elt in dbs:
		print("-> "+elt)

if(args.p):
    if(args.db):
        db = client[args.db]
        collection = db[args.p]
        printCollection(collection)

if(args.collection and args.db):
    db = client[args.db]
    collectionList = db.collection_names()
    for collect in collectionList:
        print(collect)
