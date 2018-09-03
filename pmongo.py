#!/usr/bin/python3

import datetime as date
from random import randint
from Mongo import Mongo
import argparse


HOST = ''
PORT = ***REMOVED***

parser = argparse.ArgumentParser(description="Gestion base mongodb")
groupSelect = parser.add_argument_group('Sélecteur')

parser.add_argument("-c","--collection", action="store_true",help="Affiche les collections de la base", dest="collection" )
parser.add_argument("--dbs", action="store_true", help="Affiche les bases", dest="base")


groupSelect.add_argument("-D", help="Base de donnée",metavar='Base', dest="selectBase")
groupSelect.add_argument("-C",help="Affiche la collections indiquée", metavar="COLLECTION", dest="selectCollection")


args = parser.parse_args()

mongo = Mongo(HOST, PORT)
print(args)

if(args.base):
    mongo.showDataBase()

if(args.collection):
    mongo.showListCollection(args.selectBase)

if(args.selectCollection and args.selectBase):
    mongo.printCollection(args.selectBase,args.selectCollection)
