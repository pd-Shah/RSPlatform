import click

from flask import current_app, g
from pymongo import MongoClient

from .config import MONGO_URI, DATABASE

def get_db():
    if "db" not in g:
        # Making a Connection with MongoClient
        db_client = MongoClient(MONGO_URI)
        # Getting a Database
        db = db_client[DATABASE]
        # Getting a Collection
        # collection = db['test-collection']
        g.db = db
    return g.db

def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.logout()
