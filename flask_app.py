from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pickle
from nltk.tokenize import word_tokenize  
import nltk
import json
import pymongo
nltk.download("punkt")

app = Flask(__name__)
import db
from db import *
api = Api(app)

# def parse_json(data):
#     return json.loads(dumps(data))

puppies = []
def find_features(document):
        with open("word_features.txt", "rb") as fp:
            word_features = pickle.load(fp)
        words = word_tokenize(document)
        features = {}
        for w in word_features:
            features[w] = (w in words)
        return features

# class Sentiment(Resource):
    
#     def get(self,text):  
#         print(text)
#         loaded_model = pickle.load(open("SentiAnalysis.sav", 'rb'))

#         feats = find_features(text)
        
#         result = loaded_model.classify(feats)
#         print(result)
#         return result
                    


# api.add_resource(Sentiment, '/sentiment/<string:text>')
@app.route("/",methods=['GET'])
def get1():
    return("flask server is up and running")



@app.route("/test/<string:text>",methods=['POST'])
def get(text):  
        print(text)
        loaded_model = pickle.load(open("SentiAnalysis2.sav", 'rb'))
        feats = find_features(text)        
        result = loaded_model.classify(feats)
        user_collection.insert_one({"status": result})
        print(result)
        return jsonify({'ModelResponse': result})
    

@app.route("/test2",methods=['GET'])
def getty():
    positive = user_collection.find({"status":"positive"}).count()     
    negative = user_collection.find({"status":"negative"}).count()    
    print(positive)
    print(negative)
    res = {}
    res['Positive'] = positive
    res['Negative'] = negative
    
    return jsonify(res)
    

if __name__ == '__main__':
    app.run(debug=True,port=5500)
