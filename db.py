from flask import Flask
import pymongo

#from app import app
app=Flask(__name__)

CONNECTION_STRING = "mongodb+srv://cpdb:cpkadb@cluster0.aczbb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client['sentimentApi']
# user_collection = pymongo.collection.Collection(db, 'helloCollection')
user_collection = db['sentiment Analysis']

# CONNECTION_STRING = "mongodb+srv://test:test@flask-mongodb-atlas-1g8po.mongodb.net/test?retryWrites=true&w=majority"
# client = pymongo.MongoClient(CONNECTION_STRING)
# db = client.get_database('flask_mongodb_atlas')
# user_collection = pymongo.collection.Collection(db, 'user_collection')