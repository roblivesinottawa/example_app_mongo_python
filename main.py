from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DB'] = 'mongopydb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mongopydb'

mongo = PyMongo(app)


@app.route('/comics', methods=['GET'])
def get_all_comics():
    comic = mongo.db.comics
    output = []
    for com in comic.find():
        output.append({'name': com['name'], 'publisher': com['publisher']})
    return jsonify({'result': output})
