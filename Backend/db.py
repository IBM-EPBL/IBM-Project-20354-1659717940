from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING = 'mongodb+srv://ibmproject:Jk6ZTnyGvhiEMr21@ibmproject.573tpup.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('heart_disease_prediction')
users = pymongo.collection.Collection(db, 'Users')
