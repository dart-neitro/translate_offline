"""
tests with MongoDB
"""
__author__ = 'neitro'

from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')

# get database
db = client['test-database']

collection = db['test-collection']

client.close()


