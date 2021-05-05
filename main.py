from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DB'] = 'mongopydb'
app.config['MONGO_URI'] = '*********************'

mongo = PyMongo(app)


@app.route('/comics', methods=['GET'])
def get_all_comics():
    comic = mongo.db.comics
    output = []
    for com in comic.find():
        output.append({'name': com['name'], 'publisher': com['publisher']})
    return jsonify({'result': output})


@app.route('/comic', methods=['GET'])
def get_one_comic(name):
    comic = mongo.db.comics
    comic_ = comic.find_one({'name': name})
    if comic_:
        output = ({'name': comic_['name'], 'publisher': comic_['publisher']})
    else:
        output = "No such name"
    return jsonify({'result': output})


@app.route('/comic', methods=['POST'])
def add_comic():
    comic = mongo.db.comics
    name = request.json['name']
    publisher = request.json['publisher']
    comic_id = comic.insert({'name': name, 'publisher': publisher})
    new_comic = comic.find_one({'_id': comic_id})
    output = ({'name': new_comic['name'], 'publisher': new_comic['publisher']})
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
