import pymongo
from flask import Flask, jsonify
from flask_cors import CORS

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.nyc_311_data 

app = Flask(__name__)
CORS(app)
@app.route("/api/v1/<mycollection>")
def get_api(mycollection):
	data = list(db[mycollection].find({}, {'_id': False}))
	return jsonify(data)

if __name__ == "__main__":
    app.run()