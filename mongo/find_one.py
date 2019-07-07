"""Connect to MongoDB Atlas and print record from collection"""

import yaml
from pymongo import MongoClient

with open('path/to/conf.yaml', 'r') as f:
    conf = yaml.load(f, Loader=yaml.SafeLoader)

user, password, cluster = [conf[k] for k in ('user', 'password', 'cluster')]
client = MongoClient(f'mongodb+srv://{user}:{password}@{cluster}.gcp.mongodb.net/test?retryWrites=true&w=majority')

collection = client.db.my_collection
print(collection.find_one())