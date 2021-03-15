from flask import Flask
import pymongo

app=Flask(__name__)

CONNECTION_STRING = "mongodb+srv://swarnabha:swarnabhaflask@cluster0.sbgtv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)

db = client.get_database('sentimentApi')
user_collection = pymongo.collection.Collection(db, 'sentimentAnalysis')

