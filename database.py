import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file (if using one)
load_dotenv()

# Get MongoDB connection string from environment variable
mongo_uri = os.getenv("MONGO_URI")  # Replace "MONGO_URI" with your actual environment variable name

if not mongo_uri:
    raise ValueError("MONGO_URI environment variable is not set")

# MongoDB connection
client = MongoClient(mongo_uri)
db = client["invoice_db"]  # Database name
invoice_collection = db["invoices"]  # Collection name