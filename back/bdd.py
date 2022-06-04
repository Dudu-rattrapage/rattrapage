
from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client["wiki-country"]
countries = db.countries
data = {"nom": "Allemagne","capitale": "Berlin", "id":3}
countries.insert_one(data)
