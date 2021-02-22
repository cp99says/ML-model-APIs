from flask import Flask
import pymongo

#from app import app
app=Flask(__name__)

#CONNECTION_STRING = "mongodb+srv://in:in@cluster0.p9jmu.mongodb.net/geny?retryWrites=true&w=majority"
CONNECTION_STRING = "mongodb+srv://swarnabha:swarnabhaflask@cluster0.sbgtv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
#CONNECTION_STRING = "mongodb+srv://hellocp:flaskapi2@cluster0.ynvts.mongodb.net/sentimentApi?retryWrites=true&w=majority"
#CONNECTION_STRING = "mongodb://localhost:27017/sentimental2"
client = pymongo.MongoClient(CONNECTION_STRING)
#db = client['sentimentApi']
# user_collection = pymongo.collection.Collection(db, 'helloCollection')
#user_collection = db['sentiment Analysis']
db = client.get_database('sentimentApi')
user_collection = pymongo.collection.Collection(db, 'sentimentAnalysis')

# CONNECTION_STRING = "mongodb+srv://test:test@flask-mongodb-atlas-1g8po.mongodb.net/test?retryWrites=true&w=majority"
# client = pymongo.MongoClient(CONNECTION_STRING)
# db = client.get_database('flask_mongodb_atlas')
# user_collection = pymongo.collection.Collection(db, 'user_collection')