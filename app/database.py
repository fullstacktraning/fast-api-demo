# MongoClient, used to connect to database
from pymongo import MongoClient
# used to load .env file
from dotenv import load_dotenv
# read variables from environmental file
import os
# load .env file to memory
load_dotenv()
# create client object
client = MongoClient(os.getenv("MONGO_URL"))
# access pranat_db
db = client["pranat_db"]
# creates / connect to collection
users_collection = db["users"]
laptops_collection = db["laptops"]
