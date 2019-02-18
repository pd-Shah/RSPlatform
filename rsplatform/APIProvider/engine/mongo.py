import click

from flask import current_app, g
from flask_pymongo import PyMongo

def get_db():
    if "mongo" not in g:
        g.mongo = PyMongo(current_app)
    return g.mongo
