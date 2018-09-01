#!/usr/bin/python3

import datetime as date
from random import randint
from Mongo import Mongo
import argparse


HOST = ''
PORT = ***REMOVED***

parser = argparse.ArgumentParser(description="Gestion base mongodb")
parser.add_argument("-D",'--db', help="Base de donnée", default="apiwatchTest", metavar='Base', dest="selectBase")
parser.add_argument("-c","--collection", action="store_true",help="Affiche les collections de la base", dest="collection" )
parser.add_argument("-C",help="Affiche la collections indiquée", metavar="COLLECTION", dest="selectCollection")
parser.add_argument("--dbs", action="store_true", help="Affiche les bases", dest="base")
args = parser.parse_args()

mongo = Mongo(HOST, PORT)
print(args)

if(args.base):
    mongo.showDataBase()

if(args.collection):
    mongo.showListCollection(args.selectBase)
