from pymongo import MongoClient

client = MongoClient("mongodb+srv://karthikm20:12345677@cluster0.qrb6qry.mongodb.net/?retryWrites=true&w=majority")
db = client.answers