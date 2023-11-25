from pymongo import MongoClient
from datetime import datetime
import hashlib

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

'''
Function : Connecting to the Mongo DB 
'''
# Access MongoDB URI from environment variables
mongo_uri = os.getenv('MONGODB_URI')
mongo_db_name = os.getenv('MONGODB_DBNAME_01')
mongo_collection_name = os.getenv('MONGODB_COLLECTION_01')

def connect_to_mongodb():
    try:
        # Create a MongoClient
        client = MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_collection_name]
        return collection

    except Exception as e:
        print(f'Error connecting to MongoDB: {e}')
        return None

'''
Function : To generate the Hashed Password
'''
def hash_password(password):
    # Use a strong hashing algorithm, such as SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

'''
Function : To check if the use exists + Save the login date-time in the DB
'''
def authenticate_user(userid, password):
    try:

        user_details = connect_to_mongodb()
        hashed_password = hash_password(password)
        user = user_details.find_one({'userid': userid, 'hashed_password': hashed_password})
        if user:
            # Update last login date
            user_details.update_one({'_id': user['_id']}, {'$set': {'date_of_last_login': datetime.utcnow()}})
            return True
        else:
            return False

    except Exception as e:
        print(f'Error: {e}')
        return None



'''
Function : Main 
'''
if __name__ == "__main__":
    # Test getting user details
    userid_to_check = 'user70@example.com'
    password_to_check = 'securepassword70'

    user_data = authenticate_user(userid_to_check, password_to_check)