from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pickle
from nltk.tokenize import word_tokenize  
import nltk
import json
import pymongo
from flask_cors import CORS, cross_origin
#nltk.download("punkt")
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


import db
from db import *
api = Api(app)

# def parse_json(data):
#     return json.loads(dumps(data))

puppies = []
risk_words = {
    'not good' : 'bad',
    'not bad' : 'good',
    'not nice' : 'bad',
    'hate' : 'bad'
}
def find_features(document):
        with open("word_features_final.txt", "rb") as fp:
            word_features = pickle.load(fp)
        document = document.lower()
        words = word_tokenize(document)
        document_words = set(words)
        features = {}
        for w in word_features:
           features['contains({})'.format(w)] = (w in document_words)
        for w in risk_words.keys():
         if w in document:
          features['contains({})'.format(risk_words[w])] = (w in document)
          if w != 'hate':
            features['contains({})'.format(w.split()[1])] = False
        return features

# with open("word_features_final.txt", "rb") as fp:
#             word_features = pickle.load(fp)
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
@cross_origin()
def get1():
    return("flask server is up and running")



@app.route("/test/<string:text>",methods=['POST'])
@cross_origin()
def get(text):  
        print(text)
        loaded_model = pickle.load(open("SentiAnalysisfinal.sav", 'rb'))
        feats = find_features(text)        
        result = loaded_model.classify(feats)
        user_collection.insert_one({"status": result})
        print(result)
        return jsonify({'ModelResponse': result})
    

@app.route("/test2",methods=['GET'])
@cross_origin()
def getty():
    positive = user_collection.count_documents({"status":"positive"})    
    negative = user_collection.count_documents({"status":"negative"})
    print(positive)
    print(negative)
    res = {}
    res['Positive'] = positive
    res['Negative'] = negative    
    return jsonify(res)
    # db.db.collection.insert_one({"name": "John"})
    # return "Connected to the data base!"
    
    

if __name__ == '__main__':
    app.run(debug=True,port=5500,host='0.0.0.0')
