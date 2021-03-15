from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pickle
from nltk.tokenize import word_tokenize  
import nltk
import json
import pymongo
from flask_cors import CORS, cross_origin
nltk.download("punkt")
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


import db
from db import *
api = Api(app)



    

if __name__ == '__main__':
    app.run(debug=True,port=5500,host='0.0.0.0')
