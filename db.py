from flask import Flask
import pymongo

#from app import app
app=Flask(__name__)

CONNECTION_STRING = "mongodb://localhost:27017/sentimentApi"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client['sentimentApi']
# user_collection = pymongo.collection.Collection(db, 'helloCollection')
user_collection = db['collection']