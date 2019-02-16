from flask import Flask
from pymongo import MongoClient
import os

db_client = MongoClient(host="0.0.0.0", port=27017)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "service is running..."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
