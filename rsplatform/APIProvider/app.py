import os
from pymongo import MongoClient

from flask import Flask

from resources.user import user_blueprint

db_client = MongoClient(host="0.0.0.0", port=27017)

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix="/api/v1")

@app.route('/', methods=["GET"])
def hello_world():
    return "server is running..."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
