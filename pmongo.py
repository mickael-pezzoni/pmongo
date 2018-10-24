#!/usr/bin/python3

import datetime as date
from random import randint
from Mongo import Mongo
import argparse


HOST = "localhost"
PORT = 27017

parser = argparse.ArgumentParser(description="Gestion base mongodb")
groupSelect = parser.add_argument_group('Sélecteur')

groupWarning = parser.add_mutually_exclusive_group()

parser.add_argument("-c","--collection", action="store_true",help="Affiche les collections de la base", dest="collection" )
parser.add_argument("--dbs", action="store_true", help="Affiche les bases", dest="base")
parser.add_argument("-p",action="store_true", help="Affiche la collection ciblée", dest="printCollection")
#parser.add_argument("--all", help="Toute les collections", action="store_true", dest="all")
parser.add_argument("--export", help="Exporter une ou plusieurs base", action="store_true", dest="export")
parser.add_argument("-D", help="Base de donnée",metavar='Base', dest="selectBase")

groupWarning.add_argument("--all", help="Toute les collections", action="store_true", dest="all")
groupWarning.add_argument("-C",help="selectionne la collection", metavar="COLLECTION", dest="selectCollection")


args = parser.parse_args()

mongo = Mongo(HOST, PORT)

if(args.base):
    mongo.showDataBase()

if(args.collection):
    mongo.showListCollection(args.selectBase)

if(args.selectCollection and args.selectBase and args.printCollection):
    print(mongo.printCollection(args.selectBase,args.selectCollection))

if(args.selectBase and args.all and args.export):
    mongo.exportAllCollectioni(args.selectBase)

if(args.selectBase and args.selectCollection and args.export):
    mongo.exportOneCollection(args.selectBase, args.selectCollection)