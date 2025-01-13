from pymongo import MongoClient

# MongoDB connection
client = MongoClient("process.env.Mongodb")
db = client["invoice_db"]  # Database name
invoice_collection = db["invoices"]  # Collection name