from pymongo import MongoClient, ASCENDING
import os
from dotenv import load_dotenv
from datetime import datetime
import hashlib
from faker import Faker

# Load environment variables from .env file
load_dotenv()

'''
Function : Connecting to the Mongo DB 
'''
# Access MongoDB URI from environment variables
mongo_uri = os.getenv('MONGODB_URI')
mongo_db_name = os.getenv('MONGODB_DBNAME_01')
mongo_collection_name = os.getenv('MONGODB_COLLECTION_01')

# Connecting to the DB based
client = MongoClient(mongo_uri)
db = client[mongo_db_name]
user_details = db[mongo_collection_name]

# Create an index on the 'userid' field with ASCENDING order (default is ASCENDING)
user_details.create_index([('userid', ASCENDING)], unique=True)

'''
Funtion : take random name from the list
'''
def hash_password(password):
    # Use a strong hashing algorithm, such as SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

'''
Funtion : To check if the userid exists in the DB or not
'''
def is_userid_unique(userid):
    # Check if the userid is already present in the database
    return user_details.find_one({'userid': userid}) is None

'''
Funtion : To take random name from the list
'''
def generate_random_user_name():
    # Use faker to generate random names for plants, animals, or mountains
    fake = Faker()
    return fake.random_element(elements=(
        'Dog', 'Cow', 'Cat', 'Horse', 'Donkey', 'Tiger', 'Lion', 'Panther',
        'Leopard', 'Cheetah', 'Bear', 'Elephant', 'Polar bear', 'Turtle', 'Tortoise', 'Crocodile',
        'Rabbit', 'Porcupine', 'Hare', 'Hen', 'Pigeon', 'Albatross', 'Crow', 'Fish',
        'Dolphin', 'Frog', 'Whale', 'Alligator', 'Eagle', 'Flying squirrel', 'Ostrich', 'Fox',
        'Goat', 'Jackal', 'Emu', 'Armadillo', 'Eel', 'Goose', 'Arctic fox', 'Wolf',
        'Beagle', 'Gorilla', 'Chimpanzee', 'Monkey', 'Beaver', 'Orangutan', 'Antelope', 'Bat',
        'Badger', 'Giraffe', 'Hermit Crab', 'Giant Panda', 'Hamster', 'Cobra', 'Hammerhead shark', 'Camel',
        'Hawk', 'Deer', 'Chameleon', 'Hippopotamus', 'Jaguar', 'Chihuahua', 'King Cobra', 'Ibex',
        'Lizard', 'Koala', 'Kangaroo', 'Iguana', 'Llama', 'Chinchillas', 'Dodo', 'Jellyfish',
        'Rhinoceros', 'Hedgehog', 'Zebra', 'Possum', 'Wombat', 'Bison', 'Bull', 'Buffalo',
        'Sheep', 'Meerkat', 'Mouse', 'Otter', 'Sloth', 'Owl', 'Vulture', 'Flamingo',
        'Racoon', 'Mole', 'Duck', 'Swan', 'Lynx', 'Monitor lizard', 'Elk', 'Boar',
        'Lemur', 'Mule', 'Baboon', 'Mammoth', 'Blue whale', 'Rat', 'Snake', 'Peacock'
   ))

'''
Funtion : To create the user in the DB
'''
def create_user(email, password, language='English'):
    # Check if the userid (email) is unique
    if not is_userid_unique(email):
        print(f"Error: User cannot be created. The userid '{email}' already exists in the database. Please Login instead!")
        return

    hashed_password = hash_password(password)
    user_name = generate_random_user_name()

    user_data = {
        'email': email,
        'hashed_password': hashed_password,
        'user_name': user_name,
        'userid': email,  # Use email as userid
        'date_of_creation': datetime.utcnow(),
        'date_of_last_login': None,
        'date_of_last_update': None,
        'language_preference': language
    }
    user_details.insert_one(user_data)
    print(f"User with userid '{email}' created in the database.")
    return
